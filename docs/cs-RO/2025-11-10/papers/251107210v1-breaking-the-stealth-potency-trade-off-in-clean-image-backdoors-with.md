---
layout: default
title: Breaking the Stealth-Potency Trade-off in Clean-Image Backdoors with Generative Trigger Optimization
---

# Breaking the Stealth-Potency Trade-off in Clean-Image Backdoors with Generative Trigger Optimization

**arXiv**: [2511.07210v1](https://arxiv.org/abs/2511.07210) | [PDF](https://arxiv.org/pdf/2511.07210.pdf)

**作者**: Binyan Xu, Fan Yang, Di Tang, Xilin Dai, Kehuan Zhang

---

## 💡 一句话要点

**提出生成式干净图像后门框架以解决攻击隐蔽性与有效性权衡问题**

**关键词**: `干净图像后门攻击` `生成对抗网络` `触发器优化` `模型安全` `隐蔽攻击` `多任务适应`

## 📋 核心要点

1. 现有干净图像后门攻击需高毒化率，导致清洁精度显著下降，影响隐蔽性
2. 使用条件InfoGAN优化触发器，识别自然图像特征作为隐蔽有效触发器
3. 实验显示在多种数据集、架构和任务中，清洁精度下降小于1%，且抗防御强

## 📄 摘要（原文）

> Clean-image backdoor attacks, which use only label manipulation in training
> datasets to compromise deep neural networks, pose a significant threat to
> security-critical applications. A critical flaw in existing methods is that the
> poison rate required for a successful attack induces a proportional, and thus
> noticeable, drop in Clean Accuracy (CA), undermining their stealthiness. This
> paper presents a new paradigm for clean-image attacks that minimizes this
> accuracy degradation by optimizing the trigger itself. We introduce Generative
> Clean-Image Backdoors (GCB), a framework that uses a conditional InfoGAN to
> identify naturally occurring image features that can serve as potent and
> stealthy triggers. By ensuring these triggers are easily separable from benign
> task-related features, GCB enables a victim model to learn the backdoor from an
> extremely small set of poisoned examples, resulting in a CA drop of less than
> 1%. Our experiments demonstrate GCB's remarkable versatility, successfully
> adapting to six datasets, five architectures, and four tasks, including the
> first demonstration of clean-image backdoors in regression and segmentation.
> GCB also exhibits resilience against most of the existing backdoor defenses.

