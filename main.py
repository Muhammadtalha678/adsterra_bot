import asyncio
import random
import urllib.request
import re
from playwright.async_api import async_playwright

def get_free_proxies():
    """GitHub Open Pools se live free working proxies nikalne ka engine"""
    print("Fetching active free proxies from live open GitHub source pools...")
    proxies = []
    try:
        urls = [
            "https://githubusercontent.com",
            "https://githubusercontent.com"
        ]
        headers = {'User-Agent': 'Mozilla/5.0'}
        for url in urls:
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=15) as response:
                    html = response.read().decode('utf-8')
                    found = re.findall(r'\d+\.\d+\.\d+\.\d+:\d+', html)
                    proxies.extend(found)
            except Exception as inner_err:
                print(f"Skipping unstable server endpoint... Log: {inner_err}")
    except Exception as e:
        print(f"Global proxy engine update warning: {e}")
        
    if not proxies:
        return ["161.35.70.244:80", "138.197.148.215:80"] 
    return list(set(proxies))

async def run_advanced_impression(cycle_number, proxy_pool):
    chosen_platform = random.choice(["Windows", "MacOS", "Linux"])
    chrome_args = [
        "--disable-blink-features=AutomationControlled",
        "--ignore-certificate-errors",
        "--allow-running-insecure-content",
        "--no-sandbox",
        "--disable-web-security",
        "--disable-popup-blocking"
    ]
    widths = [1366, 1440, 1536, 1920]
    heights = [768, 900, 864, 1080]
    chosen_width = random.choice(widths)
    chosen_height = random.choice(heights)

    print(f"Device Spoofed As: {chosen_platform.upper()} | Resolution: {chosen_width}x{chosen_height}")
    
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True, args=chrome_args)
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        
        selected_proxy = random.choice(proxy_pool)
        print(f"📡 Rotating Session Node IP to Free Proxy: {selected_proxy}")

        context_config = {
            "viewport": {"width": chosen_width, "height": chosen_height},
            "user_agent": user_agent,
            "ignore_https_errors": True,
            "proxy": {"server": f"http://{selected_proxy}"}
        }
        
        try:
            context = await browser.new_context(**context_config)
            page = await context.new_page()
            await page.add_init_script("delete navigator.__proto__.webdriver;")
            
            print("Navigating to Main App Layout Dashboard...")
            url = "https://youtube-video-download-automation.vercel.app"
            
            await page.goto(url, wait_until="domcontentloaded", timeout=40000)
            await page.wait_for_timeout(6000)

            # --- POP-UP GENERATOR ---
            print("Executing Hardware Emulation Mouse Click to open the target Ad tab...")
            async with context.expect_page(timeout=15000) as new_page_info:
                cx = int(chosen_width / 2)
                cy = int(chosen_height / 2)
                await page.mouse.move(cx, cy)
                await page.mouse.click(cx, cy, delay=120)
            
            new_tab = await new_page_info.value
            print("🔥 SUCCESS! Pop-up blocker bypassed. New Ad Tab Intercepted!")
            await new_tab.bring_to_front()
            
            print("Waiting 12 seconds for the ad redirection pipelines to settle...")
            await asyncio.sleep(12)
            
            # --- CRASH-PROOF NATURAL SCROLL LOOP ---
            print("Simulating human reading & scrolling on active ad destination viewport...")
            current_scroll = 0
            for step in range(8):
                scroll_step = random.randint(250, 500)
                await new_tab.mouse.wheel(delta_x=0, delta_y=scroll_step)
                current_scroll += scroll_step
                print(f"Active Scrolling Step #{step+1}: Scrolled down {current_scroll}px")
                await new_tab.wait_for_timeout(random.randint(2500, 4500))

        except Exception as e:
            print(f"⚠️ Cycle Skip Notice: Proxy connection dropped or timeout occurred. Error: {e}")

        print(f"Impression Cycle #{cycle_number} Closed Safely.")
        await browser.close()

async def main():
    proxy_pool = get_free_proxies()
    print(f"Successfully cached {len(proxy_pool)} active dynamic proxies into bot engine storage.")
    
    cycle = 1
    for i in range(5):
        print(f"\n--- Starting Cloud Impression Cycle #{cycle} ---")
        try:
            await run_advanced_impression(cycle, proxy_pool)
        except Exception as e:
            print(f"Cycle execution alert: {e}")
        
        await asyncio.sleep(8)
        cycle += 1

if __name__ == "__main__":
    asyncio.run(main())
