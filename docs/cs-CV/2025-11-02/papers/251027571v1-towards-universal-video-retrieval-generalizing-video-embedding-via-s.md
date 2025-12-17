---
layout: default
title: Towards Universal Video Retrieval: Generalizing Video Embedding via Synthesized Multimodal Pyramid Curriculum
---

# Towards Universal Video Retrieval: Generalizing Video Embedding via Synthesized Multimodal Pyramid Curriculum

**arXiv**: [2510.27571v1](https://arxiv.org/abs/2510.27571) | [PDF](https://arxiv.org/pdf/2510.27571.pdf)

**作者**: Zhuoning Guo, Mingxin Li, Yanzhao Zhang, Dingkun Long, Pengjun Xie, Xiaowen Chu

---

## 💡 一句话要点

**提出通用视频检索框架，通过多模态金字塔课程训练解决泛化能力不足问题**

**关键词**: `通用视频检索` `多模态嵌入` `课程学习` `零样本泛化` `基准设计` `数据合成`

## 📋 核心要点

1. 核心问题：现有视频检索基准狭窄，抑制多维度泛化能力，缺乏诊断性评估
2. 方法要点：设计UVRB基准、合成大规模数据、引入模态金字塔课程训练GVE模型
3. 实验或效果：GVE在UVRB上实现零样本泛化SOTA，揭示流行基准预测能力差

## 📄 摘要（原文）

> The prevailing video retrieval paradigm is structurally misaligned, as narrow
> benchmarks incentivize correspondingly limited data and single-task training.
> Therefore, universal capability is suppressed due to the absence of a
> diagnostic evaluation that defines and demands multi-dimensional
> generalization. To break this cycle, we introduce a framework built on the
> co-design of evaluation, data, and modeling. First, we establish the Universal
> Video Retrieval Benchmark (UVRB), a suite of 16 datasets designed not only to
> measure performance but also to diagnose critical capability gaps across tasks
> and domains. Second, guided by UVRB's diagnostics, we introduce a scalable
> synthesis workflow that generates 1.55 million high-quality pairs to populate
> the semantic space required for universality. Finally, we devise the Modality
> Pyramid, a curriculum that trains our General Video Embedder (GVE) by
> explicitly leveraging the latent interconnections within our diverse data.
> Extensive experiments show GVE achieves state-of-the-art zero-shot
> generalization on UVRB. In particular, our analysis reveals that popular
> benchmarks are poor predictors of general ability and that partially relevant
> retrieval is a dominant but overlooked scenario. Overall, our co-designed
> framework provides a practical path to escape the limited scope and advance
> toward truly universal video retrieval.

