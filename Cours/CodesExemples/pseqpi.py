def par_picks(n,npu):
   from concurrent.futures import ProcessPoolExecutor
   pool = ProcessPoolExecutor(npu)
   nlocal=int(n/npu)
   futures = [pool.submit(seqpi.picks,nlocal)] *npu
   results = [f.result() for f in futures]
   return results
