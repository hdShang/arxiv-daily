---
layout: default
title: LCMem: A Universal Model for Robust Image Memorization Detection
---

# LCMem: A Universal Model for Robust Image Memorization Detection

**arXiv**: [2512.14421v1](https://arxiv.org/abs/2512.14421) | [PDF](https://arxiv.org/pdf/2512.14421.pdf)

**作者**: Mischa Dombrowski, Felix Nützel, Bernhard Kainz

**分类**: cs.CV

**发布日期**: 2025-12-16

**🔗 代码/项目**: [GITHUB](https://github.com/MischaD/LCMem)

---

## 💡 一句话要点

**提出LCMem模型，通过统一重识别和复制检测任务，解决跨域图像记忆检测的鲁棒性问题。**

**关键词**: `图像记忆检测` `隐私审计` `重识别` `复制检测` `跨域模型` `对比学习` `生成模型安全` `数据共享保护`

## 📋 核心要点

1. 核心问题：现有隐私审计方法在跨域泛化能力差，缺乏可靠的记忆检测机制和定量评估，限制了隐私保护数据共享的应用。
2. 方法要点：将记忆检测统一为重识别和复制检测的交叉问题，采用两阶段训练策略，先学习身份一致性，再融入增强鲁棒的复制检测。
3. 实验或效果：在六个数据集上，LCMem在重识别任务提升高达16个百分点，复制检测任务提升高达30个百分点，显著提高检测可靠性。

## 📝 摘要（中文）

生成图像建模的最新进展已实现足以欺骗人类专家的视觉真实感，但其在隐私保护数据共享方面的潜力仍未得到充分理解。一个核心障碍是缺乏可靠的记忆检测机制、有限的定量评估以及现有隐私审计方法在跨域中的泛化能力差。为解决这一问题，我们提出将记忆检测视为重识别和复制检测交叉点的统一问题，其互补目标涵盖身份一致性和增强鲁棒的复制检测，并引入潜在对比记忆网络（LCMem），这是一个在两项任务上联合评估的跨域模型。LCMem通过两阶段训练策略实现这一点：首先学习身份一致性，然后纳入增强鲁棒的复制检测。在六个基准数据集上，LCMem在重识别任务上提升了高达16个百分点，在复制检测任务上提升了高达30个百分点，实现了更可靠的大规模记忆检测。我们的结果表明，现有隐私过滤器性能有限且鲁棒性不足，突显了更强保护机制的需求。LCMem为跨域隐私审计设定了新标准，提供可靠且可扩展的记忆检测。代码和模型公开可用。

## 🔬 方法详解

LCMem是一个跨域模型，整体框架基于潜在对比记忆网络，将记忆检测视为重识别和复制检测的统一任务。关键技术创新点包括：采用两阶段训练策略，第一阶段专注于学习身份一致性，第二阶段结合增强鲁棒的复制检测，通过对比学习优化特征表示。与现有方法的主要区别在于，LCMem整合了互补任务，避免了传统隐私审计方法的领域依赖性和泛化不足问题，实现了更鲁棒的跨域检测能力。

## 📊 实验亮点

在六个基准数据集上，LCMem在重识别任务中性能提升高达16个百分点，复制检测任务提升高达30个百分点，显著优于现有隐私过滤器，证明了其在跨域记忆检测中的鲁棒性和可扩展性。

## 🎯 应用场景

该研究可应用于隐私保护数据共享、生成模型审计、图像版权保护等领域，为跨域隐私审计提供可靠工具，帮助识别和防止敏感图像数据的未经授权使用，提升数据安全性和合规性。

## 📄 摘要（原文）

> Recent advances in generative image modeling have achieved visual realism sufficient to deceive human experts, yet their potential for privacy preserving data sharing remains insufficiently understood. A central obstacle is the absence of reliable memorization detection mechanisms, limited quantitative evaluation, and poor generalization of existing privacy auditing methods across domains. To address this, we propose to view memorization detection as a unified problem at the intersection of re-identification and copy detection, whose complementary goals cover both identity consistency and augmentation-robust duplication, and introduce Latent Contrastive Memorization Network (LCMem), a cross-domain model evaluated jointly on both tasks. LCMem achieves this through a two-stage training strategy that first learns identity consistency before incorporating augmentation-robust copy detection. Across six benchmark datasets, LCMem achieves improvements of up to 16 percentage points on re-identification and 30 percentage points on copy detection, enabling substantially more reliable memorization detection at scale. Our results show that existing privacy filters provide limited performance and robustness, highlighting the need for stronger protection mechanisms. We show that LCMem sets a new standard for cross-domain privacy auditing, offering reliable and scalable memorization detection. Code and model is publicly available at https://github.com/MischaD/LCMem.

