---
layout: default
title: MVCustom: Multi-View Customized Diffusion via Geometric Latent Rendering and Completion
---

# MVCustom: Multi-View Customized Diffusion via Geometric Latent Rendering and Completion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13702" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13702v1</a>
  <a href="https://arxiv.org/pdf/2510.13702.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13702v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.13702v1', 'MVCustom: Multi-View Customized Diffusion via Geometric Latent Rendering and Completion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minjung Shin, Hyunin Cho, Sooyeon Go, Jin-Hwa Kim, Youngjung Uh

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-15

**备注**: Project page: https://minjung-s.github.io/mvcustom

---

## 💡 一句话要点

**MVCustom：通过几何潜在渲染和补全实现多视角定制化扩散模型**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `多视角生成` `定制化扩散模型` `几何一致性` `特征场表示` `深度感知渲染` `潜在空间补全` `时空注意力`

## 📋 核心要点

1. 现有方法难以兼顾多视角几何一致性和prompt定制化，限制了可控生成模型的发展。
2. MVCustom通过特征场表示学习主体几何，并利用时空注意力增强的扩散模型保证多视角一致性。
3. 深度感知渲染和一致性感知补全技术，确保了定制主体与背景在多视角下的几何对齐。

## 📝 摘要（中文）

本文提出了一种新的任务：多视角定制化，旨在联合实现多视角相机姿态控制和定制化。现有多视角生成模型缺乏定制化能力，而定制化模型又缺乏显式的视角控制，难以统一。针对定制化训练数据稀缺的问题，现有依赖大规模数据集的多视角生成模型难以泛化到不同的提示词。为此，我们提出了MVCustom，一种基于扩散的新框架，专门用于实现多视角一致性和定制化保真度。在训练阶段，MVCustom使用特征场表示学习主体的身份和几何形状，并结合增强了密集时空注意力的文本到视频扩散骨干网络，利用时间连贯性来实现多视角一致性。在推理阶段，我们引入了两种新技术：深度感知特征渲染显式地强制执行几何一致性，一致性感知潜在补全确保了定制主体和周围背景的精确透视对齐。大量实验表明，MVCustom是唯一能够同时实现忠实的多视角生成和定制化的框架。

## 🔬 方法详解

**问题定义**：现有方法要么缺乏多视角定制能力，要么缺乏显式的视角控制，无法同时实现多视角一致性和定制化。此外，定制化任务通常面临训练数据稀缺的问题，使得依赖大规模数据集的模型难以泛化到新的prompt。

**核心思路**：MVCustom的核心思路是利用扩散模型强大的生成能力，结合几何先验和时空注意力机制，实现多视角一致的定制化生成。通过特征场表示学习主体的几何信息，并利用深度信息和一致性约束来保证不同视角下生成结果的一致性。

**技术框架**：MVCustom包含训练和推理两个阶段。在训练阶段，使用文本到视频的扩散模型作为骨干网络，并引入密集时空注意力机制来增强多视角一致性。同时，利用特征场表示学习主体的几何信息。在推理阶段，首先使用深度感知特征渲染将学习到的特征场渲染到不同的视角，然后使用一致性感知潜在补全模块来确保定制主体和周围背景的精确透视对齐。

**关键创新**：MVCustom的关键创新在于：1) 提出了多视角定制化这一新任务；2) 结合特征场表示和扩散模型，实现了多视角一致的定制化生成；3) 提出了深度感知特征渲染和一致性感知潜在补全两种新技术，显式地强制执行几何一致性。

**关键设计**：MVCustom使用文本到视频的扩散模型作为骨干网络，并引入了密集时空注意力机制。特征场表示采用MLP结构，用于学习主体的几何信息。深度感知特征渲染模块利用深度信息将特征场渲染到不同的视角。一致性感知潜在补全模块使用一个额外的扩散模型来补全背景，并确保与定制主体的一致性。损失函数包括扩散模型的重建损失、特征场的几何损失和一致性损失。

## 📊 实验亮点

实验结果表明，MVCustom在多视角定制化任务上取得了显著的性能提升。与其他基线方法相比，MVCustom能够生成具有更高质量和更好一致性的多视角图像，同时能够忠实地反映用户的定制化需求。实验还验证了深度感知特征渲染和一致性感知潜在补全两种技术的有效性。

## 🎯 应用场景

MVCustom可应用于虚拟现实、增强现实、游戏开发等领域，例如，用户可以根据自己的照片或文本描述，生成具有多视角一致性的3D虚拟形象，并将其应用于各种虚拟场景中。该技术还可以用于生成具有特定风格和视角的艺术作品，为创意设计提供新的可能性。

## 📄 摘要（原文）

> Multi-view generation with camera pose control and prompt-based customization are both essential elements for achieving controllable generative models. However, existing multi-view generation models do not support customization with geometric consistency, whereas customization models lack explicit viewpoint control, making them challenging to unify. Motivated by these gaps, we introduce a novel task, multi-view customization, which aims to jointly achieve multi-view camera pose control and customization. Due to the scarcity of training data in customization, existing multi-view generation models, which inherently rely on large-scale datasets, struggle to generalize to diverse prompts. To address this, we propose MVCustom, a novel diffusion-based framework explicitly designed to achieve both multi-view consistency and customization fidelity. In the training stage, MVCustom learns the subject's identity and geometry using a feature-field representation, incorporating the text-to-video diffusion backbone enhanced with dense spatio-temporal attention, which leverages temporal coherence for multi-view consistency. In the inference stage, we introduce two novel techniques: depth-aware feature rendering explicitly enforces geometric consistency, and consistent-aware latent completion ensures accurate perspective alignment of the customized subject and surrounding backgrounds. Extensive experiments demonstrate that MVCustom is the only framework that simultaneously achieves faithful multi-view generation and customization.

