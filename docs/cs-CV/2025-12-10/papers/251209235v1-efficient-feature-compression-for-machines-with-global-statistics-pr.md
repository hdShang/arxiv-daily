---
layout: default
title: Efficient Feature Compression for Machines with Global Statistics Preservation
---

# Efficient Feature Compression for Machines with Global Statistics Preservation

**arXiv**: [2512.09235v1](https://arxiv.org/abs/2512.09235) | [PDF](https://arxiv.org/pdf/2512.09235.pdf)

**作者**: Md Eimran Hossain Eimon, Hyomin Choi, Fabien Racapé, Mateen Ulhaq, Velibor Adzic, Hari Kalva, Borko Furht

---

## 💡 一句话要点

**提出基于Z-score归一化的特征压缩方法，以提升MPEG FCM标准中的机器视觉任务性能**

**关键词**: `特征压缩` `Z-score归一化` `MPEG FCM标准` `拆分推理` `机器视觉任务`

## 📋 核心要点

1. 针对AI模型拆分推理中的中间特征数据传输，提出高效压缩需求
2. 采用Z-score归一化方法，在解码端有效恢复压缩特征，替代现有缩放方法
3. 实验显示平均比特率降低17.09%，对象跟踪任务最高达65.69%，且不牺牲任务精度

## 📄 摘要（原文）

> The split-inference paradigm divides an artificial intelligence (AI) model into two parts. This necessitates the transfer of intermediate feature data between the two halves. Here, effective compression of the feature data becomes vital. In this paper, we employ Z-score normalization to efficiently recover the compressed feature data at the decoder side. To examine the efficacy of our method, the proposed method is integrated into the latest Feature Coding for Machines (FCM) codec standard under development by the Moving Picture Experts Group (MPEG). Our method supersedes the existing scaling method used by the current standard under development. It both reduces the overhead bits and improves the end-task accuracy. To further reduce the overhead in certain circumstances, we also propose a simplified method. Experiments show that using our proposed method shows 17.09% reduction in bitrate on average across different tasks and up to 65.69% for object tracking without sacrificing the task accuracy.

