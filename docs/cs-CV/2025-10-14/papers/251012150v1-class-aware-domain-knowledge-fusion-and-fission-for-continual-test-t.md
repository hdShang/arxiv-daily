---
layout: default
title: Class-aware Domain Knowledge Fusion and Fission for Continual Test-Time Adaptation
---

# Class-aware Domain Knowledge Fusion and Fission for Continual Test-Time Adaptation

**arXiv**: [2510.12150v1](https://arxiv.org/abs/2510.12150) | [PDF](https://arxiv.org/pdf/2510.12150.pdf)

**作者**: Jiahuan Zhou, Chao Zhu, Zhenyu Cui, Zichen Liu, Xu Zou, Gang Hua

---

## 💡 一句话要点

**提出类感知域知识融合与分裂方法以解决持续测试时适应中的知识遗忘与干扰问题**

**关键词**: `持续测试时适应` `知识融合` `知识分裂` `类感知域提示` `动态知识管理` `ImageNet-C`

## 📋 核心要点

1. 核心问题：现有方法在持续测试时适应中易导致新知识学习不足和历史知识干扰，引发性能下降
2. 方法要点：设计知识分裂模块分离新域知识，知识融合模块高效合并新旧知识，动态积累判别性知识
3. 实验或效果：在ImageNet-C数据集上验证方法有效性，优于其他方法

## 📄 摘要（原文）

> Continual Test-Time Adaptation (CTTA) aims to quickly fine-tune the model
> during the test phase so that it can adapt to multiple unknown downstream
> domain distributions without pre-acquiring downstream domain data. To this end,
> existing advanced CTTA methods mainly reduce the catastrophic forgetting of
> historical knowledge caused by irregular switching of downstream domain data by
> restoring the initial model or reusing historical models. However, these
> methods are usually accompanied by serious insufficient learning of new
> knowledge and interference from potentially harmful historical knowledge,
> resulting in severe performance degradation. To this end, we propose a
> class-aware domain Knowledge Fusion and Fission method for continual test-time
> adaptation, called KFF, which adaptively expands and merges class-aware domain
> knowledge in old and new domains according to the test-time data from different
> domains, where discriminative historical knowledge can be dynamically
> accumulated. Specifically, considering the huge domain gap within streaming
> data, a domain Knowledge FIssion (KFI) module is designed to adaptively
> separate new domain knowledge from a paired class-aware domain prompt pool,
> alleviating the impact of negative knowledge brought by old domains that are
> distinct from the current domain. Besides, to avoid the cumulative computation
> and storage overheads from continuously fissioning new knowledge, a domain
> Knowledge FUsion (KFU) module is further designed to merge the fissioned new
> knowledge into the existing knowledge pool with minimal cost, where a greedy
> knowledge dynamic merging strategy is designed to improve the compatibility of
> new and old knowledge while keeping the computational efficiency. Extensive
> experiments on the ImageNet-C dataset verify the effectiveness of our proposed
> method against other methods.

