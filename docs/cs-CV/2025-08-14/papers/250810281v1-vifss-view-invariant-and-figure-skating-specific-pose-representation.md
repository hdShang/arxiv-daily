---
layout: default
title: "VIFSS: View-Invariant and Figure Skating-Specific Pose Representation Learning for Temporal Action Segmentation"
---

# VIFSS: View-Invariant and Figure Skating-Specific Pose Representation Learning for Temporal Action Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10281" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10281v1</a>
  <a href="https://arxiv.org/pdf/2508.10281.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10281v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10281v1', 'VIFSS: View-Invariant and Figure Skating-Specific Pose Representation Learning for Temporal Action Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ryota Tanaka, Tomohiro Suzuki, Keisuke Fujii

**分类**: cs.CV

**发布日期**: 2025-08-14

---

## 💡 一句话要点

**提出VIFSS以解决花样滑冰动作分割问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `时间动作分割` `花样滑冰` `三维姿态表示` `对比学习` `细粒度标注` `动作识别` `体育分析`

## 📋 核心要点

1. 现有的时间动作分割方法在花样滑冰领域面临数据不足和未考虑三维特性的问题。
2. 本文提出VIFSS方法，通过对比学习和动作分类相结合，解决了跳跃动作的表示学习问题。
3. 实验结果表明，本文方法在元素级TAS上达到了92%以上的F1@50，显示出显著的性能提升。

## 📝 摘要（中文）

理解视频中的人类动作在多个领域中至关重要，尤其是在体育分析中。花样滑冰中，准确识别滑冰者跳跃的类型和时机对于客观评估表现至关重要。然而，这一任务通常需要专家级知识，因为跳跃过程复杂且细致。尽管近期有研究尝试使用时间动作分割（TAS）自动化此任务，但存在两个主要限制：标注数据不足，以及现有方法未考虑跳跃动作的三维特性和程序结构。本文提出了一种新的TAS框架，明确结合了跳跃动作的三维特性和语义程序。我们提出了一种新颖的视角不变、花样滑冰特定的姿态表示学习方法（VIFSS），并构建了第一个专门用于花样滑冰跳跃的公开3D姿态数据集FS-Jump3D。通过广泛实验验证了该框架的有效性，方法在元素级TAS上达到了92%以上的F1@50。

## 🔬 方法详解

**问题定义**：本文旨在解决花样滑冰跳跃动作的时间动作分割问题。现有方法面临标注数据不足和未考虑跳跃动作的三维特性与程序结构的痛点。

**核心思路**：提出视角不变、花样滑冰特定的姿态表示学习方法（VIFSS），结合对比学习进行预训练，再通过动作分类进行微调，以有效学习跳跃动作的特征。

**技术框架**：整体框架包括两个主要阶段：首先进行视角不变的对比预训练，使用FS-Jump3D数据集；然后进行细粒度标注的微调，标记“入场（准备）”和“落地”阶段，以帮助模型学习跳跃的程序结构。

**关键创新**：最重要的创新在于构建了FS-Jump3D数据集，并提出了细粒度的标注方案，使得模型能够更好地理解跳跃动作的复杂性和程序性。与现有方法相比，VIFSS显著提高了对跳跃动作的识别能力。

**关键设计**：在模型设计中，采用了对比损失函数以增强视角不变性，同时在微调阶段引入了细粒度标注，确保模型能有效学习跳跃的不同阶段。

## 📊 实验亮点

实验结果显示，本文方法在元素级时间动作分割上达到了92%以上的F1@50，显著优于现有基线。这表明在有限的微调数据下，视角不变的对比预训练能够有效提升模型性能，具有良好的实际应用前景。

## 🎯 应用场景

该研究的潜在应用领域包括体育分析、运动员训练评估和比赛裁判辅助等。通过准确识别花样滑冰中的跳跃动作，能够为教练和运动员提供客观的数据支持，进而提升训练效果和比赛表现。未来，该方法还可扩展到其他运动项目的动作识别与分析中。

## 📄 摘要（原文）

> Understanding human actions from videos plays a critical role across various domains, including sports analytics. In figure skating, accurately recognizing the type and timing of jumps a skater performs is essential for objective performance evaluation. However, this task typically requires expert-level knowledge due to the fine-grained and complex nature of jump procedures. While recent approaches have attempted to automate this task using Temporal Action Segmentation (TAS), there are two major limitations to TAS for figure skating: the annotated data is insufficient, and existing methods do not account for the inherent three-dimensional aspects and procedural structure of jump actions. In this work, we propose a new TAS framework for figure skating jumps that explicitly incorporates both the three-dimensional nature and the semantic procedure of jump movements. First, we propose a novel View-Invariant, Figure Skating-Specific pose representation learning approach (VIFSS) that combines contrastive learning as pre-training and action classification as fine-tuning. For view-invariant contrastive pre-training, we construct FS-Jump3D, the first publicly available 3D pose dataset specialized for figure skating jumps. Second, we introduce a fine-grained annotation scheme that marks the ``entry (preparation)'' and ``landing'' phases, enabling TAS models to learn the procedural structure of jumps. Extensive experiments demonstrate the effectiveness of our framework. Our method achieves over 92% F1@50 on element-level TAS, which requires recognizing both jump types and rotation levels. Furthermore, we show that view-invariant contrastive pre-training is particularly effective when fine-tuning data is limited, highlighting the practicality of our approach in real-world scenarios.

