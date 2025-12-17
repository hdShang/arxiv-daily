---
layout: default
title: Design Space Exploration of DMA based Finer-Grain Compute Communication Overlap
---

# Design Space Exploration of DMA based Finer-Grain Compute Communication Overlap

**arXiv**: [2512.10236v1](https://arxiv.org/abs/2512.10236) | [PDF](https://arxiv.org/pdf/2512.10236.pdf)

**作者**: Shagnik Pal, Shaizeen Aga, Suchita Pati, Mahzabeen Islam, Lizy K. John

---

## 💡 一句话要点

**提出FiCCO细粒度计算通信重叠方法，利用DMA优化分布式ML性能**

**关键词**: `分布式机器学习` `计算通信重叠` `细粒度调度` `DMA卸载` `性能优化` `设计空间探索`

## 📋 核心要点

1. 针对分布式ML中数据依赖通信与计算暴露导致的性能损失问题
2. 提出细粒度重叠FiCCO，扩展设计空间并分析操作分解效率损失
3. 基于DMA卸载通信，定制化调度实现最高1.6倍加速，启发式准确率达81%

## 📄 摘要（原文）

> As both ML training and inference are increasingly distributed, parallelization techniques that shard (divide) ML model across GPUs of a distributed system, are often deployed. With such techniques, there is a high prevalence of data-dependent communication and computation operations where communication is exposed, leaving as high as 1.7x ideal performance on the table. Prior works harness the fact that ML model state and inputs are already sharded, and employ careful overlap of individual computation/communication shards. While such coarse-grain overlap is promising, in this work, we instead make a case for finer-grain compute-communication overlap which we term FiCCO, where we argue for finer-granularity, one-level deeper overlap than at shard-level, to unlock compute/communication overlap for a wider set of network topologies, finer-grain dataflow and more. We show that FiCCO opens up a wider design space of execution schedules than possible at shard-level alone. At the same time, decomposition of ML operations into smaller operations (done in both shard-based and finer-grain techniques) causes operation-level inefficiency losses. To balance the two, we first present a detailed characterization of these inefficiency losses, then present a design space of FiCCO schedules, and finally overlay the schedules with concomitant inefficiency signatures. Doing so helps us design heuristics that frameworks and runtimes can harness to select bespoke FiCCO schedules based on the nature of underlying ML operations. Finally, to further minimize contention inefficiencies inherent with operation overlap, we offload communication to GPU DMA engines. We evaluate several scenarios from realistic ML deployments and demonstrate that our proposed bespoke schedules deliver up to 1.6x speedup and our heuristics provide accurate guidance in 81% of unseen scenarios.

