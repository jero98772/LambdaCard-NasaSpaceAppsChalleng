import asyncio
from rtlsdr import RtlSdr

async def streaming():
    sdr = RtlSdr()

    async for samples in sdr.stream():
        print(samples)        
        # do something with samples
        # ...

    # to stop streaming:
    await sdr.stop()
    sdr.close()
loop = asyncio.get_event_loop()
loop.run_until_complete(streaming())