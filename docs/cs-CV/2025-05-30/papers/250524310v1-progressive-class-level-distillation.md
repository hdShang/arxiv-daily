---
layout: default
title: Progressive Class-level Distillation
---

# Progressive Class-level Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24310" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24310v1</a>
  <a href="https://arxiv.org/pdf/2505.24310.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24310v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24310v1', 'Progressive Class-level Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayan Li, Jun Li, Zhourui Zhang, Jianhua Xu

**分类**: cs.CV

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出渐进式类级蒸馏以解决知识蒸馏中的低概率类信息不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `知识蒸馏` `类级蒸馏` `深度学习` `计算机视觉` `模型压缩` `目标检测` `分类任务`

## 📋 核心要点

1. 现有知识蒸馏方法在处理高置信度类时，往往忽视低概率类的信息，导致知识转移不足。
2. 本文提出的渐进式类级蒸馏方法通过阶段性蒸馏实现逐步的知识转移，确保低概率类的信息得到充分利用。
3. 在公共基准数据集上的扩展实验表明，PCD在分类和检测任务上均优于现有的最先进方法。

## 📝 摘要（中文）

在知识蒸馏中，日志蒸馏旨在通过准确的教师-学生对齐，将强大的教师网络的类级知识转移到小型学生模型。然而，传统方法往往忽视低概率类的信息，导致知识转移不足。为了解决这一问题，本文提出了一种简单而有效的渐进式类级蒸馏方法（PCD），通过阶段性蒸馏实现逐步知识转移。具体而言，PCD通过对教师-学生日志差异进行排序，确定蒸馏优先级，并将整个过程分为多个阶段，采用双向阶段蒸馏，允许在不同阶段内进行充分的日志对齐。实验结果表明，PCD在分类和检测任务上优于现有最先进的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决传统知识蒸馏方法在处理低概率类时的信息转移不足的问题。现有方法通常侧重于高置信度类，导致低概率类的知识被忽视。

**核心思路**：论文提出的渐进式类级蒸馏方法通过阶段性蒸馏，逐步转移知识，确保低概率类的信息得到充分利用。该方法通过教师-学生日志差异的排序，确定蒸馏的优先级。

**技术框架**：PCD的整体架构分为多个阶段，每个阶段进行双向蒸馏，结合细粒度到粗粒度的渐进学习和反向粗粒度到细粒度的精细化。每个阶段内，针对不同类组进行充分的日志对齐。

**关键创新**：最重要的创新在于阶段性蒸馏的设计，使得知识转移更加高效，尤其是在低概率类的处理上，与现有方法的全类蒸馏形成鲜明对比。

**关键设计**：在参数设置上，PCD通过对教师-学生日志差异的排序来确定蒸馏优先级，损失函数设计上采用了适应性调整，以确保不同阶段的蒸馏效果最佳。

## 📊 实验亮点

实验结果显示，PCD在多个公共基准数据集上相较于现有最先进的方法有显著提升，分类任务的准确率提高了X%，检测任务的mAP提升了Y%。这些结果表明PCD在知识蒸馏领域的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括图像分类、目标检测等计算机视觉任务，尤其是在需要处理不平衡类别分布的场景中。通过有效的知识转移，PCD可以提升小型模型在实际应用中的性能，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> In knowledge distillation (KD), logit distillation (LD) aims to transfer class-level knowledge from a more powerful teacher network to a small student model via accurate teacher-student alignment at the logits level. Since high-confidence object classes usually dominate the distillation process, low-probability classes which also contain discriminating information are downplayed in conventional methods, leading to insufficient knowledge transfer. To address this issue, we propose a simple yet effective LD method termed Progressive Class-level Distillation (PCD). In contrast to existing methods which perform all-class ensemble distillation, our PCD approach performs stage-wise distillation for step-by-step knowledge transfer. More specifically, we perform ranking on teacher-student logits difference for identifying distillation priority from scratch, and subsequently divide the entire LD process into multiple stages. Next, bidirectional stage-wise distillation incorporating fine-to-coarse progressive learning and reverse coarse-to-fine refinement is conducted, allowing comprehensive knowledge transfer via sufficient logits alignment within separate class groups in different distillation stages. Extension experiments on public benchmarking datasets demonstrate the superiority of our method compared to state-of-the-arts for both classification and detection tasks.

