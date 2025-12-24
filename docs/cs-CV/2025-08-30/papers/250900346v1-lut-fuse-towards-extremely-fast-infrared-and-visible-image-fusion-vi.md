---
layout: default
title: "LUT-Fuse: Towards Extremely Fast Infrared and Visible Image Fusion via Distillation to Learnable Look-Up Tables"
---

# LUT-Fuse: Towards Extremely Fast Infrared and Visible Image Fusion via Distillation to Learnable Look-Up Tables

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00346" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00346v1</a>
  <a href="https://arxiv.org/pdf/2509.00346.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00346v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00346v1', 'LUT-Fuse: Towards Extremely Fast Infrared and Visible Image Fusion via Distillation to Learnable Look-Up Tables')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xunpeng Yi, Yibing Zhang, Xinyu Xiang, Qinglong Yan, Han Xu, Jiayi Ma

**分类**: cs.CV

**发布日期**: 2025-08-30

**备注**: Accepted by ICCV 2025

**🔗 代码/项目**: [GITHUB](https://github.com/zyb5/LUT-Fuse)

---

## 💡 一句话要点

**提出LUT-Fuse以解决实时红外与可见光图像融合问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `红外图像` `可见光图像` `图像融合` `蒸馏学习` `查找表` `多模态融合` `实时处理` `高效算法`

## 📋 核心要点

1. 现有红外与可见光图像融合方法多关注性能提升，忽视实时应用的需求，导致在实际设备上应用受限。
2. 本文提出LUT-Fuse，通过蒸馏学习可学习的查找表，结合低阶近似编码与高层次上下文编码，实现快速高效的图像融合。
3. 实验结果表明，LUT-Fuse在效率上显著优于现有轻量级融合算法，处理时间通常不到其十分之一，适用于多种场景。

## 📝 摘要（中文）

当前红外与可见光图像融合的研究主要集中在提高融合性能上，往往忽视了实时融合设备的适用性。本文提出了一种新颖的方法LUT-Fuse，通过蒸馏学习可学习的查找表，实现极快的图像融合。我们开发了一种查找表结构，利用低阶近似编码和高层次的联合上下文场景编码，适合多模态融合。此外，针对多模态图像融合缺乏真实标签的问题，我们提出了高效的LUT蒸馏策略，替代传统的量化LUT方法。通过将多模态融合网络（MM-Net）的性能整合到MM-LUT模型中，我们的方法在效率和性能上取得了显著突破，通常所需时间不到当前轻量级SOTA融合算法的十分之一，确保在各种场景下的高操作速度，甚至在低功耗移动设备上也能高效运行。大量实验验证了我们融合方法的优越性、可靠性和稳定性。

## 🔬 方法详解

**问题定义**：本文旨在解决红外与可见光图像融合的实时性问题，现有方法往往在性能上有所提升，但在实际应用中速度较慢，难以满足实时设备的需求。

**核心思路**：LUT-Fuse的核心思路是通过蒸馏学习可学习的查找表，利用低阶近似编码和高层次的联合上下文场景编码，以实现快速且高效的多模态图像融合。这样的设计使得融合过程能够在保持高性能的同时，显著提升处理速度。

**技术框架**：该方法的整体架构包括查找表结构的设计、LUT蒸馏策略的实现以及与多模态融合网络（MM-Net）的结合。首先，构建查找表以适应多模态数据的特性，然后通过蒸馏策略优化查找表的学习过程。

**关键创新**：LUT-Fuse的主要创新在于引入了高效的LUT蒸馏策略，替代了传统的量化方法，使得在缺乏真实标签的情况下，依然能够有效学习到融合所需的特征。这一创新使得方法在效率和性能上均有显著提升。

**关键设计**：在设计过程中，采用了低阶近似编码和高层次上下文编码相结合的方式，确保了多模态数据的有效融合。同时，网络结构经过精心设计，以适应快速处理的需求，损失函数的选择也考虑到了融合效果的优化。

## 📊 实验亮点

实验结果显示，LUT-Fuse在处理速度上显著优于当前的轻量级SOTA融合算法，通常处理时间不到其十分之一。同时，在多模态图像融合的性能上也取得了显著提升，验证了该方法的有效性和稳定性。

## 🎯 应用场景

LUT-Fuse的研究成果在多个领域具有广泛的应用潜力，特别是在需要实时图像处理的场景，如无人驾驶、安防监控和移动设备等。其高效的融合能力能够提升多模态数据的利用效率，为实际应用提供更为可靠的支持。未来，该方法有望在更多实际场景中得到推广和应用。

## 📄 摘要（原文）

> Current advanced research on infrared and visible image fusion primarily focuses on improving fusion performance, often neglecting the applicability on real-time fusion devices. In this paper, we propose a novel approach that towards extremely fast fusion via distillation to learnable lookup tables specifically designed for image fusion, termed as LUT-Fuse. Firstly, we develop a look-up table structure that utilizing low-order approximation encoding and high-level joint contextual scene encoding, which is well-suited for multi-modal fusion. Moreover, given the lack of ground truth in multi-modal image fusion, we naturally proposed the efficient LUT distillation strategy instead of traditional quantization LUT methods. By integrating the performance of the multi-modal fusion network (MM-Net) into the MM-LUT model, our method achieves significant breakthroughs in efficiency and performance. It typically requires less than one-tenth of the time compared to the current lightweight SOTA fusion algorithms, ensuring high operational speed across various scenarios, even in low-power mobile devices. Extensive experiments validate the superiority, reliability, and stability of our fusion approach. The code is available at https://github.com/zyb5/LUT-Fuse.

