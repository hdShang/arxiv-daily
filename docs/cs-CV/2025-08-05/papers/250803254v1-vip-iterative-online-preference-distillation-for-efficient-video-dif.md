---
layout: default
title: "V.I.P. : Iterative Online Preference Distillation for Efficient Video Diffusion Models"
---

# V.I.P. : Iterative Online Preference Distillation for Efficient Video Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03254" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03254v1</a>
  <a href="https://arxiv.org/pdf/2508.03254.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03254v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03254v1', 'V.I.P. : Iterative Online Preference Distillation for Efficient Video Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jisoo Kim, Wooseok Seo, Junwan Kim, Seungho Park, Sooyeon Park, Youngjae Yu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-05

**备注**: ICCV2025 accepted

**🔗 代码/项目**: [PROJECT_PAGE](https://jiiiisoo.github.io/VIP.github.io/)

---

## 💡 一句话要点

**提出V.I.P.框架以解决视频扩散模型的高计算成本问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视频生成` `文本到视频` `蒸馏训练` `模型剪枝` `多模态学习`

## 📋 核心要点

1. 现有的蒸馏方法依赖于监督微调，导致剪枝模型无法有效匹配教师模型输出，造成质量下降。
2. 提出的ReDPO方法结合DPO和SFT，指导学生模型专注于恢复目标属性，提升整体性能。
3. 在VideoCrafter2和AnimateDiff模型上验证，分别实现36.2%和67.5%的参数减少，同时保持或超越性能。

## 📝 摘要（中文）

随着在资源受限环境中部署文本到视频（T2V）模型的兴趣日益增长，降低其高计算成本变得至关重要。现有的蒸馏方法主要依赖于监督微调（SFT），这往往导致模式崩溃，因为经过剪枝的模型无法直接匹配教师模型的输出，从而导致质量下降。为了解决这一挑战，本文提出了一种有效的蒸馏方法ReDPO，结合了DPO和SFT，指导学生模型专注于恢复目标属性，同时利用SFT提升整体性能。此外，提出了V.I.P.框架，用于过滤和策划高质量配对数据集，并采用逐步在线校准训练的方法。我们在两个领先的T2V模型上验证了该方法，分别实现了36.2%和67.5%的参数减少，同时保持或超越了完整模型的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决文本到视频模型在资源受限环境中的高计算成本问题。现有的蒸馏方法主要依赖于监督微调（SFT），这导致剪枝模型无法有效匹配教师模型的输出，最终影响生成质量。

**核心思路**：提出的ReDPO方法通过结合DPO和SFT，指导学生模型专注于恢复特定的目标属性，而不是被动模仿教师模型，从而避免模式崩溃。

**技术框架**：V.I.P.框架包括高质量配对数据集的过滤和策划，以及逐步在线校准训练的过程。整体流程分为数据准备、模型训练和性能评估三个主要阶段。

**关键创新**：最重要的创新在于将DPO与SFT相结合，形成了一种新的蒸馏策略，使得学生模型能够更有效地学习目标属性，避免了传统方法中的模式崩溃问题。

**关键设计**：在参数设置上，采用了适应性学习率和特定的损失函数，以确保模型在训练过程中的稳定性和收敛性。此外，网络结构经过优化，以适应蒸馏过程中的特定需求。

## 📊 实验亮点

实验结果显示，使用V.I.P.框架在VideoCrafter2和AnimateDiff模型上分别实现了36.2%和67.5%的参数减少，同时保持或超越了完整模型的性能，验证了方法的有效性和高效性。

## 🎯 应用场景

该研究的潜在应用领域包括影视制作、游戏开发和教育等多个领域，能够在资源受限的环境中实现高效的视频生成，具有重要的实际价值。未来，随着技术的进一步发展，可能会推动更多创新的多媒体应用和服务。

## 📄 摘要（原文）

> With growing interest in deploying text-to-video (T2V) models in resource-constrained environments, reducing their high computational cost has become crucial, leading to extensive research on pruning and knowledge distillation methods while maintaining performance. However, existing distillation methods primarily rely on supervised fine-tuning (SFT), which often leads to mode collapse as pruned models with reduced capacity fail to directly match the teacher's outputs, ultimately resulting in degraded quality. To address this challenge, we propose an effective distillation method, ReDPO, that integrates DPO and SFT. Our approach leverages DPO to guide the student model to focus on recovering only the targeted properties, rather than passively imitating the teacher, while also utilizing SFT to enhance overall performance. We additionally propose V.I.P., a novel framework for filtering and curating high-quality pair datasets, along with a step-by-step online approach for calibrated training. We validate our method on two leading T2V models, VideoCrafter2 and AnimateDiff, achieving parameter reduction of 36.2% and 67.5% each, while maintaining or even surpassing the performance of full models. Further experiments demonstrate the effectiveness of both ReDPO and V.I.P. framework in enabling efficient and high-quality video generation. Our code and videos are available at https://jiiiisoo.github.io/VIP.github.io/.

