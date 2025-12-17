---
layout: default
title: CC-FMO: Camera-Conditioned Zero-Shot Single Image to 3D Scene Generation with Foundation Model Orchestration
---

# CC-FMO: Camera-Conditioned Zero-Shot Single Image to 3D Scene Generation with Foundation Model Orchestration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.00493" class="toolbar-btn" target="_blank">📄 arXiv: 2512.00493v1</a>
  <a href="https://arxiv.org/pdf/2512.00493.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.00493v1" onclick="toggleFavorite(this, '2512.00493v1', 'CC-FMO: Camera-Conditioned Zero-Shot Single Image to 3D Scene Generation with Foundation Model Orchestration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boshi Tang, Henry Zheng, Rui Huang, Gao Huang

**分类**: cs.CV

**发布日期**: 2025-11-29

---

## 💡 一句话要点

**CC-FMO：利用基础模型编排，实现相机条件下的单图零样本3D场景生成**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D场景生成` `单图重建` `零样本学习` `基础模型` `相机条件` `姿态估计` `语义感知`

## 📋 核心要点

1. 现有单图到3D场景生成方法依赖于小数据集训练的专用模型，泛化能力不足。
2. CC-FMO提出一种相机条件下的零样本生成流程，结合语义感知向量集和结构化潜在表示，提升场景连贯性。
3. 实验结果表明，CC-FMO在生成高质量、相机对齐的3D场景方面优于现有技术水平。

## 📝 摘要（中文）

本文提出CC-FMO，一个零样本、相机条件下的单图像到3D场景生成流程，旨在同时符合输入图像中的对象布局并保持实例的保真度。CC-FMO采用混合实例生成器，将语义感知的向量集表示与细节丰富的结构化潜在表示相结合，生成在语义上合理且高质量的对象几何体。此外，CC-FMO通过简单而有效的相机条件尺度求解算法，在场景生成任务中应用基础姿态估计模型，以增强场景级别的连贯性。大量实验表明，CC-FMO能够持续生成高保真、相机对齐的组合场景，优于所有最先进的方法。

## 🔬 方法详解

**问题定义**：单张图像生成高质量3D场景是AR/VR和具身智能的关键。现有方法依赖于在小型数据集上训练的专用模型，泛化能力差。虽然大型3D基础模型在实例级别生成方面取得了显著进展，但由于不准确的物体姿态估计和空间不一致性，连贯的场景生成仍然是一个挑战。

**核心思路**：CC-FMO的核心思路是利用基础模型的力量，通过相机条件约束和混合实例生成器，实现零样本的单图到3D场景生成。通过结合语义感知的向量集表示和细节丰富的结构化潜在表示，生成语义合理且高质量的物体几何体，并利用相机条件尺度求解算法来保证场景级别的连贯性。

**技术框架**：CC-FMO的整体流程包括以下几个主要阶段：1) 输入单张图像；2) 使用语义分割模型提取图像中的物体类别和掩码；3) 使用混合实例生成器，根据物体类别和掩码生成3D物体几何体；4) 使用基础姿态估计模型估计物体的姿态；5) 使用相机条件尺度求解算法调整物体的大小和位置，以保证场景的连贯性；6) 将生成的物体组合成完整的3D场景。

**关键创新**：CC-FMO的关键创新在于：1) 提出了一种混合实例生成器，结合了语义感知的向量集表示和细节丰富的结构化潜在表示，从而生成高质量的物体几何体；2) 提出了一种相机条件尺度求解算法，能够有效地利用基础姿态估计模型，保证场景级别的连贯性；3) 实现了零样本的单图到3D场景生成，无需在特定数据集上进行训练。

**关键设计**：混合实例生成器可能包含两个分支，一个分支使用向量集表示来捕捉物体的语义信息，另一个分支使用结构化潜在表示来生成物体的细节信息。相机条件尺度求解算法可能使用最小化重投影误差或最大化场景一致性的方法来优化物体的大小和位置。损失函数可能包括几何损失、姿态损失和语义损失等。

## 📊 实验亮点

实验结果表明，CC-FMO在单图到3D场景生成任务中优于所有最先进的方法。CC-FMO能够生成高保真、相机对齐的组合场景，在场景连贯性和物体质量方面都取得了显著提升。具体的性能数据和对比基线在论文中进行了详细的展示。

## 🎯 应用场景

CC-FMO在AR/VR、机器人技术和具身智能等领域具有广泛的应用前景。例如，可以用于快速生成虚拟环境，为AR/VR应用提供内容；可以用于机器人导航和场景理解，帮助机器人更好地理解周围环境；可以用于具身智能体的训练和部署，使其能够在虚拟环境中学习和交互。该研究的未来影响在于推动3D内容生成和场景理解技术的发展。

## 📄 摘要（原文）

> High-quality 3D scene generation from a single image is crucial for AR/VR and embodied AI applications. Early approaches struggle to generalize due to reliance on specialized models trained on curated small datasets. While recent advancements in large-scale 3D foundation models have significantly enhanced instance-level generation, coherent scene generation remains a challenge, where performance is limited by inaccurate per-object pose estimations and spatial inconsistency. To this end, this paper introduces CC-FMO, a zero-shot, camera-conditioned pipeline for single-image to 3D scene generation that jointly conforms to the object layout in input image and preserves instance fidelity. CC-FMO employs a hybrid instance generator that combines semantics-aware vector-set representation with detail-rich structured latent representation, yielding object geometries that are both semantically plausible and high-quality. Furthermore, CC-FMO enables the application of foundational pose estimation models in the scene generation task via a simple yet effective camera-conditioned scale-solving algorithm, to enforce scene-level coherence. Extensive experiments demonstrate that CC-FMO consistently generates high-fidelity camera-aligned compositional scenes, outperforming all state-of-the-art methods.

