---
layout: default
title: Prompt-based Adaptation in Large-scale Vision Models: A Survey
---

# Prompt-based Adaptation in Large-scale Vision Models: A Survey

**arXiv**: [2510.13219v1](https://arxiv.org/abs/2510.13219) | [PDF](https://arxiv.org/pdf/2510.13219.pdf)

**作者**: Xi Xiao, Yunbei Zhang, Lin Zhao, Yiyang Liu, Xiaoying Liao, Zheda Mai, Xingjian Li, Xiao Wang, Hao Xu, Jihun Hamm, Xue Lin, Min Xu, Qifan Wang, Tianyang Wang, Cheng Han

---

## 💡 一句话要点

**提出提示适应统一框架，系统分类视觉模型轻量调优方法。**

**关键词**: `视觉提示调优` `提示适应框架` `轻量模型调优` `视觉语言任务` `测试时适应`

## 📋 核心要点

1. 核心问题：视觉提示与提示调优概念混淆，缺乏系统区分。
2. 方法要点：基于可学习、生成和非学习提示，按像素和令牌级分类。
3. 实验或效果：应用于医学影像、3D点云等领域，总结基准与挑战。

## 📄 摘要（原文）

> In computer vision, Visual Prompting (VP) and Visual Prompt Tuning (VPT) have
> recently emerged as lightweight and effective alternatives to full fine-tuning
> for adapting large-scale vision models within the ``pretrain-then-finetune''
> paradigm. However, despite rapid progress, their conceptual boundaries remain
> blurred, as VP and VPT are frequently used interchangeably in current research,
> reflecting a lack of systematic distinction between these techniques and their
> respective applications. In this survey, we revisit the designs of VP and VPT
> from first principles, and conceptualize them within a unified framework termed
> Prompt-based Adaptation (PA). We provide a taxonomy that categorizes existing
> methods into learnable, generative, and non-learnable prompts, and further
> organizes them by injection granularity -- pixel-level and token-level. Beyond
> the core methodologies, we examine PA's integrations across diverse domains,
> including medical imaging, 3D point clouds, and vision-language tasks, as well
> as its role in test-time adaptation and trustworthy AI. We also summarize
> current benchmarks and identify key challenges and future directions. To the
> best of our knowledge, we are the first comprehensive survey dedicated to PA's
> methodologies and applications in light of their distinct characteristics. Our
> survey aims to provide a clear roadmap for researchers and practitioners in all
> area to understand and explore the evolving landscape of PA-related research.

