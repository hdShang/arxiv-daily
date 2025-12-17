---
layout: default
title: RT-DETRv4: Painlessly Furthering Real-Time Object Detection with Vision Foundation Models
---

# RT-DETRv4: Painlessly Furthering Real-Time Object Detection with Vision Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.25257" class="toolbar-btn" target="_blank">📄 arXiv: 2510.25257v1</a>
  <a href="https://arxiv.org/pdf/2510.25257.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.25257v1" onclick="toggleFavorite(this, '2510.25257v1', 'RT-DETRv4: Painlessly Furthering Real-Time Object Detection with Vision Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zijun Liao, Yian Zhao, Xin Shan, Yu Yan, Chang Liu, Lei Lu, Xiangyang Ji, Jie Chen

**分类**: cs.CV

**发布日期**: 2025-10-29

---

## 💡 一句话要点

**RT-DETRv4：利用视觉基础模型，无痛提升实时目标检测性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `实时目标检测` `知识蒸馏` `视觉基础模型` `深度语义注入` `梯度自适应调制` `轻量级模型` `COCO数据集`

## 📋 核心要点

1. 现有实时目标检测器受限于轻量化设计，特征表达能力不足，难以进一步提升性能。
2. 论文提出一种基于视觉基础模型的蒸馏框架，通过深度语义注入和梯度引导自适应调制实现知识迁移。
3. RT-DETRv4模型在COCO数据集上取得SOTA结果，并在不同速度下均有显著的AP提升。

## 📝 摘要（中文）

实时目标检测通过精心设计的架构和优化策略取得了显著进展。然而，通过轻量级网络设计追求高速推理通常会导致特征表示能力下降，这阻碍了性能的进一步提升和实际的设备端部署。本文提出了一种经济高效且高度适应性的蒸馏框架，利用快速发展的视觉基础模型（VFMs）的能力来增强轻量级目标检测器。考虑到VFMs和资源受限的检测器之间存在显著的架构和学习目标差异，实现稳定且任务对齐的语义迁移具有挑战性。为了解决这个问题，一方面，我们引入了一个深度语义注入器（DSI）模块，该模块有助于将VFMs的高级表示集成到检测器的深层。另一方面，我们设计了一种梯度引导的自适应调制（GAM）策略，该策略根据梯度范数比率动态调整语义迁移的强度。在不增加部署和推理开销的情况下，我们的方法在各种基于DETR的模型上实现了显著且一致的性能提升，突显了其在实时检测中的实际效用。我们的新模型系列RT-DETRv4在COCO上实现了最先进的结果，在273/169/124/78 FPS的速度下，AP分数分别达到49.7/53.5/55.4/57.0。

## 🔬 方法详解

**问题定义**：论文旨在解决实时目标检测中，轻量级模型因特征表达能力不足而导致的性能瓶颈问题。现有方法为了追求速度，牺牲了模型深度和复杂度，使得检测精度难以进一步提升。同时，如何有效地将视觉基础模型（VFMs）的强大语义信息迁移到轻量级检测器中，也是一个挑战。

**核心思路**：论文的核心思路是利用视觉基础模型（VFMs）的强大特征表达能力，通过知识蒸馏的方式提升轻量级目标检测器的性能。为了解决VFMs和轻量级检测器之间的差异，论文设计了深度语义注入器（DSI）和梯度引导的自适应调制（GAM）策略，以实现更稳定和有效的知识迁移。

**技术框架**：整体框架包含一个预训练的视觉基础模型（VFM）作为教师模型，和一个轻量级目标检测器作为学生模型。DSI模块负责将VFM提取的高级语义特征注入到学生模型的深层特征中。GAM策略根据梯度信息动态调整语义迁移的强度，以避免负迁移。最终，学生模型在教师模型的指导下进行训练，从而提升检测性能。

**关键创新**：论文的关键创新在于DSI模块和GAM策略。DSI模块通过特定的网络结构设计，使得VFM的特征能够有效地融入到学生模型的特征中，弥补了学生模型特征表达能力的不足。GAM策略则通过梯度信息来动态调整知识迁移的强度，避免了VFM的特征对学生模型的训练产生干扰，从而实现了更稳定和有效的知识迁移。

**关键设计**：DSI模块的具体结构未知，但其目标是将VFM的高级语义特征注入到学生模型的深层特征中。GAM策略的关键在于如何计算梯度范数比率，并将其用于调整语义迁移的强度。具体的损失函数设计也未知，但需要保证学生模型在学习VFM知识的同时，保持自身的检测能力。

## 📊 实验亮点

RT-DETRv4模型在COCO数据集上取得了显著的性能提升，在不同的速度下均达到了SOTA水平。例如，在273 FPS的速度下，AP达到了49.7；在78 FPS的速度下，AP达到了57.0。相较于之前的RT-DETR模型，RT-DETRv4在精度和速度上都取得了显著的提升，证明了该方法的有效性。

## 🎯 应用场景

该研究成果可广泛应用于需要实时目标检测的场景，如自动驾驶、智能监控、机器人导航等。通过利用视觉基础模型的知识，可以显著提升轻量级检测器的性能，使其在资源受限的设备上也能实现高精度的目标检测。未来，该方法有望进一步推广到其他视觉任务中，例如图像分割、目标跟踪等。

## 📄 摘要（原文）

> Real-time object detection has achieved substantial progress through meticulously designed architectures and optimization strategies. However, the pursuit of high-speed inference via lightweight network designs often leads to degraded feature representation, which hinders further performance improvements and practical on-device deployment. In this paper, we propose a cost-effective and highly adaptable distillation framework that harnesses the rapidly evolving capabilities of Vision Foundation Models (VFMs) to enhance lightweight object detectors. Given the significant architectural and learning objective disparities between VFMs and resource-constrained detectors, achieving stable and task-aligned semantic transfer is challenging. To address this, on one hand, we introduce a Deep Semantic Injector (DSI) module that facilitates the integration of high-level representations from VFMs into the deep layers of the detector. On the other hand, we devise a Gradient-guided Adaptive Modulation (GAM) strategy, which dynamically adjusts the intensity of semantic transfer based on gradient norm ratios. Without increasing deployment and inference overhead, our approach painlessly delivers striking and consistent performance gains across diverse DETR-based models, underscoring its practical utility for real-time detection. Our new model family, RT-DETRv4, achieves state-of-the-art results on COCO, attaining AP scores of 49.7/53.5/55.4/57.0 at corresponding speeds of 273/169/124/78 FPS.

