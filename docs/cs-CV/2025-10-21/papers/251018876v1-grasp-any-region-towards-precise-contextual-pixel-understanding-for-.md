---
layout: default
title: Grasp Any Region: Towards Precise, Contextual Pixel Understanding for Multimodal LLMs
---

# Grasp Any Region: Towards Precise, Contextual Pixel Understanding for Multimodal LLMs

**arXiv**: [2510.18876v1](https://arxiv.org/abs/2510.18876) | [PDF](https://arxiv.org/pdf/2510.18876.pdf)

**作者**: Haochen Wang, Yuhao Wang, Tao Zhang, Yikang Zhou, Yanwei Li, Jiacong Wang, Ye Tian, Jiahao Meng, Zilong Huang, Guangcan Mai, Anran Wang, Yunhai Tong, Zhuochen Wang, Xiangtai Li, Zhaoxiang Zhang

---

## 💡 一句话要点

**提出Grasp Any Region以解决多模态大模型在区域级视觉理解中忽略全局上下文的问题**

**关键词**: `多模态大模型` `区域级视觉理解` `RoI特征对齐` `组合推理` `基准测试` `零样本迁移`

## 📋 核心要点

1. 核心问题：多模态大模型在复杂场景中难以进行细粒度分析和对象间关系建模，现有区域级方法忽视全局上下文
2. 方法要点：引入RoI对齐特征重放技术，支持精确感知、多提示交互建模和组合推理
3. 实验或效果：GAR-1B在多个基准测试中超越现有模型，GAR-8B在零样本视频任务中表现优异

## 📄 摘要（原文）

> While Multimodal Large Language Models (MLLMs) excel at holistic
> understanding, they struggle in capturing the dense world with complex scenes,
> requiring fine-grained analysis of intricate details and object
> inter-relationships. Region-level MLLMs have been a promising step. However,
> previous attempts are generally optimized to understand given regions in
> isolation, neglecting crucial global contexts. To address this, we introduce
> Grasp Any Region (GAR) for comprehen- sive region-level visual understanding.
> Empowered by an effective RoI-aligned feature replay technique, GAR supports
> (1) precise perception by leveraging necessary global contexts, and (2)
> modeling interactions between multiple prompts. Together, it then naturally
> achieves (3) advanced compositional reasoning to answer specific free-form
> questions about any region, shifting the paradigm from passive description to
> active dialogue. Moreover, we construct GAR-Bench, which not only provides a
> more accurate evaluation of single-region comprehension, but also, more
> importantly, measures interactions and complex reasoning across multiple
> regions. Extensive experiments have demonstrated that GAR-1B not only maintains
> the state-of-the-art captioning capabilities, e.g., outperforming DAM-3B +4.5
> on DLC-Bench, but also excels at modeling relationships between multiple
> prompts with advanced comprehension capabilities, even surpassing InternVL3-78B
> on GAR-Bench-VQA. More importantly, our zero-shot GAR-8B even outperforms
> in-domain VideoRefer-7B on VideoRefer-BenchQ, indicating its strong
> capabilities can be easily transferred to videos.

