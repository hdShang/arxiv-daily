---
layout: default
title: Intra-class Patch Swap for Self-Distillation
---

# Intra-class Patch Swap for Self-Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14124" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14124v1</a>
  <a href="https://arxiv.org/pdf/2505.14124.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14124v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14124v1', 'Intra-class Patch Swap for Self-Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongjun Choi, Eun Som Jeon, Ankita Shukla, Pavan Turaga

**分类**: cs.CV

**发布日期**: 2025-05-20

**备注**: Accepted for publication in Neurocomputing

**DOI**: [10.1016/j.neucom.2025.130408](https://doi.org/10.1016/j.neucom.2025.130408)

**🔗 代码/项目**: [GITHUB](https://github.com/hchoi71/Intra-class-Patch-Swap)

---

## 💡 一句话要点

**提出基于类内补丁交换的自蒸馏方法以简化知识蒸馏**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `知识蒸馏` `自蒸馏` `类内补丁交换` `深度学习` `计算机视觉`

## 📋 核心要点

1. 现有的知识蒸馏方法依赖于预训练的教师网络，导致内存需求高、训练成本增加和选择教师模型的困难。
2. 论文提出了一种无教师的自蒸馏框架，利用类内补丁交换增强来模拟教师-学生动态，简化了蒸馏过程。
3. 实验结果显示，该方法在多个任务上均优于传统的知识蒸馏和自蒸馏方法，表明增强设计的重要性。

## 📝 摘要（中文）

知识蒸馏（KD）是一种将大型深度学习模型压缩为适合边缘设备的小型网络的有效技术。然而，传统的KD框架依赖于预训练的高容量教师网络，这带来了内存/存储需求增加、额外训练成本以及选择合适教师模型的模糊性等挑战。尽管无教师蒸馏（自蒸馏）作为一种有前景的替代方案出现，但许多现有方法仍依赖于架构修改或复杂的训练过程，限制了其通用性和效率。为了解决这些局限性，我们提出了一种基于无教师蒸馏的新框架，使用单一学生网络，无需任何辅助组件、架构修改或额外可学习参数。我们的方法基于一种简单而有效的增强技术，称为类内补丁交换增强，通过生成具有不同置信度的类内样本对，模拟单一模型中的教师-学生动态，并应用实例间蒸馏来对齐其预测分布。我们的实验表明，该方法在图像分类、语义分割和目标检测任务中均优于现有的自蒸馏基线和传统的基于教师的KD方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决传统知识蒸馏方法中对高容量教师网络的依赖，带来的内存和训练成本问题，以及选择合适教师模型的困难。

**核心思路**：提出一种基于类内补丁交换的自蒸馏方法，通过在单一学生网络中生成类内样本对，模拟教师-学生的动态关系，从而简化蒸馏过程。

**技术框架**：整体架构包括一个学生网络和一个类内补丁交换增强模块。该模块生成不同置信度的样本对，并通过实例间蒸馏对其预测分布进行对齐。

**关键创新**：最重要的创新在于提出了类内补丁交换增强，这一方法不需要额外的教师网络或复杂的架构修改，具有模型无关性和易实现性。

**关键设计**：该方法仅需一个增强函数，且在损失函数设计上采用了实例间蒸馏策略，确保了样本对的预测分布能够有效对齐。整体设计简洁，易于在不同模型上应用。

## 📊 实验亮点

实验结果表明，该方法在图像分类、语义分割和目标检测任务中均显著优于现有的自蒸馏基线和传统的知识蒸馏方法，具体提升幅度达到X%（具体数据需根据实验结果填写）。

## 🎯 应用场景

该研究的潜在应用场景包括图像分类、语义分割和目标检测等计算机视觉任务。通过简化知识蒸馏过程，该方法能够有效提升边缘设备上的模型性能，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Knowledge distillation (KD) is a valuable technique for compressing large deep learning models into smaller, edge-suitable networks. However, conventional KD frameworks rely on pre-trained high-capacity teacher networks, which introduce significant challenges such as increased memory/storage requirements, additional training costs, and ambiguity in selecting an appropriate teacher for a given student model. Although a teacher-free distillation (self-distillation) has emerged as a promising alternative, many existing approaches still rely on architectural modifications or complex training procedures, which limit their generality and efficiency.
>   To address these limitations, we propose a novel framework based on teacher-free distillation that operates using a single student network without any auxiliary components, architectural modifications, or additional learnable parameters. Our approach is built on a simple yet highly effective augmentation, called intra-class patch swap augmentation. This augmentation simulates a teacher-student dynamic within a single model by generating pairs of intra-class samples with varying confidence levels, and then applying instance-to-instance distillation to align their predictive distributions. Our method is conceptually simple, model-agnostic, and easy to implement, requiring only a single augmentation function. Extensive experiments across image classification, semantic segmentation, and object detection show that our method consistently outperforms both existing self-distillation baselines and conventional teacher-based KD approaches. These results suggest that the success of self-distillation could hinge on the design of the augmentation itself. Our codes are available at https://github.com/hchoi71/Intra-class-Patch-Swap.

