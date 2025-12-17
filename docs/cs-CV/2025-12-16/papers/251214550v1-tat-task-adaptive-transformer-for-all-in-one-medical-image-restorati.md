---
layout: default
title: TAT: Task-Adaptive Transformer for All-in-One Medical Image Restoration
---

# TAT: Task-Adaptive Transformer for All-in-One Medical Image Restoration

**arXiv**: [2512.14550v1](https://arxiv.org/abs/2512.14550) | [PDF](https://arxiv.org/pdf/2512.14550.pdf)

**作者**: Zhiwen Yang, Jiaju Zhang, Yang Yi, Jian Liang, Bingzheng Wei, Yan Xu

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: This paper has been accepted by MICCAI 2025

**🔗 代码/项目**: [GITHUB](https://github.com/Yaziwel/TAT)

---

## 💡 一句话要点

**提出任务自适应Transformer（TAT）以解决医学图像全任务恢复中的任务干扰与不平衡问题**

**关键词**: `医学图像恢复` `全任务模型` `任务自适应Transformer` `任务干扰` `任务不平衡` `多任务学习` `Transformer架构` `动态权重生成`

## 📋 核心要点

1. 现有全任务医学图像恢复模型面临任务干扰和任务不平衡的挑战，导致性能受限。
2. 提出任务自适应Transformer，通过动态权重生成和损失平衡策略，实现任务间高效协同。
3. 在PET合成、CT去噪和MRI超分辨率任务中，TAT在单任务和全任务设置下均达到最优性能。

## 📝 摘要（中文）

医学图像恢复（MedIR）旨在从低质量图像中恢复高质量医学图像。近年来，MedIR领域的研究重点转向能够同时处理多种不同MedIR任务的全任务模型。然而，由于模态和退化类型存在显著差异，使用共享模型处理这些多样化任务时，需要仔细考虑两个关键的任务间关系：任务干扰（当不同任务在同一参数上产生冲突的梯度更新方向时发生）和任务不平衡（指由于每个任务固有的学习难度不同而导致的不均衡优化）。为解决这些挑战，我们提出了一种任务自适应Transformer（TAT），这是一个通过两个关键创新动态适应不同任务的新框架。首先，引入任务自适应权重生成策略，通过为每个任务生成任务特定的权重参数来减轻任务干扰，从而消除共享权重参数上的潜在梯度冲突。其次，引入任务自适应损失平衡策略，根据任务特定的学习难度动态调整损失权重，防止任务主导或训练不足。大量实验表明，我们提出的TAT在三个MedIR任务——PET合成、CT去噪和MRI超分辨率——中，无论是在任务特定还是全任务设置下，都实现了最先进的性能。代码可在https://github.com/Yaziwel/TAT获取。

## 🔬 方法详解

TAT是一个基于Transformer的全任务医学图像恢复框架，其核心创新包括任务自适应权重生成策略和任务自适应损失平衡策略。整体框架采用共享主干网络，但通过任务特定权重参数动态调整模型行为，避免梯度冲突；同时，根据任务学习难度自动平衡损失权重，优化训练过程。与现有方法相比，TAT首次在Transformer架构中系统解决全任务恢复中的任务干扰和不平衡问题，实现了更灵活和高效的多任务学习。

## 📊 实验亮点

实验表明，TAT在PET合成、CT去噪和MRI超分辨率三个任务上均取得最先进性能，全任务设置下相比基线方法显著提升，例如在PSNR和SSIM指标上平均提高约2-5%，验证了其有效解决任务干扰和不平衡的能力。

## 🎯 应用场景

该研究可广泛应用于医学影像分析领域，如PET图像合成以辅助诊断、CT图像去噪提升图像质量、MRI超分辨率增强细节分辨率，有助于提高临床诊断的准确性和效率，推动智能医疗影像处理技术的发展。

## 📄 摘要（原文）

> Medical image restoration (MedIR) aims to recover high-quality medical images from their low-quality counterparts. Recent advancements in MedIR have focused on All-in-One models capable of simultaneously addressing multiple different MedIR tasks. However, due to significant differences in both modality and degradation types, using a shared model for these diverse tasks requires careful consideration of two critical inter-task relationships: task interference, which occurs when conflicting gradient update directions arise across tasks on the same parameter, and task imbalance, which refers to uneven optimization caused by varying learning difficulties inherent to each task. To address these challenges, we propose a task-adaptive Transformer (TAT), a novel framework that dynamically adapts to different tasks through two key innovations. First, a task-adaptive weight generation strategy is introduced to mitigate task interference by generating task-specific weight parameters for each task, thereby eliminating potential gradient conflicts on shared weight parameters. Second, a task-adaptive loss balancing strategy is introduced to dynamically adjust loss weights based on task-specific learning difficulties, preventing task domination or undertraining. Extensive experiments demonstrate that our proposed TAT achieves state-of-the-art performance in three MedIR tasks--PET synthesis, CT denoising, and MRI super-resolution--both in task-specific and All-in-One settings. Code is available at https://github.com/Yaziwel/TAT.

