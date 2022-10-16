from rtlsdr import RtlSdr

def sdrIsConected():
	try:
		sdr = RtlSdr()
		val=True
	except:
		val=False
	return val

def main():
	if sdrIsConected(): print("coneted")
	else: print("no coneted")
if __name__ == '__main__':
	main()