# Qualified workers

def select_qualified_worker(mturk_res):
    df = pd.DataFrame(data=mturk_res)
    
    # get unique worker ids
    
    workers = df['WorkerId'].unique() 
    percents = []
    
    
    for worker in workers:
        wdf = df.loc[df["WorkerId"]==worker]
        percent = float(wdf["LifetimeApprovalRate"].values[0].split(" ")[0].strip('%'))
        lifetimehits = int(wdf["LifetimeApprovalRate"].values[0].split(" ")[1][1:].split('/')[0])
        if percent > 99 and lifetimehits >= 100:
          percents.append((worker,percent))
    percents.sort(key=lambda x:x[0])
    return percents