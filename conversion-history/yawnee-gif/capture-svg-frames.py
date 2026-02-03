#!/usr/bin/env python3
"""
Capture SVG animation frames at specific times to compare with original GIF frames.
"""

import os
import asyncio
from playwright.async_api import async_playwright

# Frame timings (in milliseconds)
frame_durations = [1500, 10, 500, 150, 200, 200, 200, 200, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 300, 100, 10, 250, 10, 250, 10, 250]

# Calculate cumulative times
cumulative_times = [0]
for duration in frame_durations:
    cumulative_times.append(cumulative_times[-1] + duration)

total_duration = cumulative_times[-1]

async def capture_svg_frames():
    """Capture SVG frames at specific animation times."""

    # Create output directory
    output_dir = "svg-frames"
    os.makedirs(output_dir, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={"width": 300, "height": 300})
        page = await context.new_page()

        # Create an HTML page that embeds the SVG with controls
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    background: white;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    width: 300px;
                    height: 300px;
                }
                #svg-container {
                    width: 120px;
                    height: 120px;
                }
                svg {
                    width: 100%;
                    height: 100%;
                }
            </style>
        </head>
        <body>
            <div id="svg-container"></div>
            <script>
                // Load the SVG
                fetch('yawnee-animated-v2.1.svg')
                    .then(response => response.text())
                    .then(svgText => {
                        document.getElementById('svg-container').innerHTML = svgText;
                        window.svgLoaded = true;
                    });

                // Function to pause animation at specific time
                window.pauseAnimationAt = function(timeMs) {
                    const svg = document.querySelector('svg');
                    if (!svg) return;

                    // Set current time and pause
                    svg.setCurrentTime(timeMs / 1000);
                    svg.pauseAnimations();

                    return true;
                };
            </script>
        </body>
        </html>
        """

        # Save HTML file
        with open("capture-frame-helper.html", "w") as f:
            f.write(html_content)

        # Load the page
        await page.goto(f"file://{os.getcwd()}/capture-frame-helper.html")

        # Wait for SVG to load
        await page.wait_for_function("window.svgLoaded === true", timeout=5000)
        await page.wait_for_timeout(500)  # Extra wait for animations to initialize

        print(f"Capturing {len(frame_durations)} frames...")

        for frame_num in range(len(frame_durations)):
            time_ms = cumulative_times[frame_num]

            # Pause animation at this time
            await page.evaluate(f"window.pauseAnimationAt({time_ms})")
            await page.wait_for_timeout(100)  # Wait for animation to settle

            # Take screenshot of just the SVG container
            svg_container = await page.query_selector("#svg-container")
            screenshot_path = f"{output_dir}/svg-frame-{frame_num:02d}.png"
            await svg_container.screenshot(path=screenshot_path)

            print(f"  Frame {frame_num}: {time_ms}ms -> {screenshot_path}")

        await browser.close()

    print(f"\n✓ Captured {len(frame_durations)} frames to {output_dir}/")
    print(f"  Size: 120×120px (matching test size)")

if __name__ == "__main__":
    asyncio.run(capture_svg_frames())
