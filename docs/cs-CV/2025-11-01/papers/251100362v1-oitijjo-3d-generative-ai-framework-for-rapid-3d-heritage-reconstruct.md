---
layout: default
title: Oitijjo-3D: Generative AI Framework for Rapid 3D Heritage Reconstruction from Street View Imagery
---

# Oitijjo-3D: Generative AI Framework for Rapid 3D Heritage Reconstruction from Street View Imagery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.00362" class="toolbar-btn" target="_blank">📄 arXiv: 2511.00362v1</a>
  <a href="https://arxiv.org/pdf/2511.00362.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00362v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.00362v1', 'Oitijjo-3D: Generative AI Framework for Rapid 3D Heritage Reconstruction from Street View Imagery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Momen Khandoker Ope, Akif Islam, Mohd Ruhul Ameen, Abu Saleh Musa Miah, Md Rashedul Islam, Jungpil Shin

**分类**: cs.CV, cs.AI, cs.GR

**发布日期**: 2025-11-01

**备注**: 6 Pages, 4 figures, 2 Tables, Submitted to ICECTE 2026

---

## 💡 一句话要点

**Oitijjo-3D：利用街景图像的快速3D遗产重建生成式AI框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D重建` `文化遗产保护` `生成式AI` `街景图像` `多模态视觉推理`

## 📋 核心要点

1. 传统3D数字化方法（如摄影测量或LiDAR扫描）成本高昂，需要专业人员和现场访问，在发展中国家难以实施。
2. Oitijjo-3D利用公开的街景图像，通过多模态视觉推理和神经图像到3D生成，快速重建文化遗产的3D模型。
3. 实验表明，Oitijjo-3D在显著降低成本和技术门槛的同时，保持了视觉和结构上的高保真度。

## 📝 摘要（中文）

本文提出Oitijjo-3D，一个免费的生成式AI框架，旨在普及3D文化遗产保护。针对孟加拉国文化遗产修复面临的资源和技术专业知识匮乏的双重挑战，该框架利用公开可用的谷歌街景图像，通过一个两阶段流程重建遗产结构的3D模型。第一阶段，使用Gemini 2.5 Flash Image进行多模态视觉推理，实现结构-纹理合成；第二阶段，通过Hexagen进行神经图像到3D的生成，恢复几何结构。该系统在几秒钟内生成照片级真实、度量一致的重建结果，与传统的运动结构重建（Structure-from-Motion）流程相比，速度显著提升，且无需任何专用硬件或专家监督。在Ahsan Manzil、Choto Sona Mosque和Paharpur等标志性建筑上的实验表明，Oitijjo-3D在大幅降低经济和技术门槛的同时，保留了视觉和结构上的保真度。通过将开放图像转化为数字遗产，这项工作将遗产保护重新定义为一种社区驱动、AI辅助的文化延续行为，特别适用于资源有限的国家。

## 🔬 方法详解

**问题定义**：论文旨在解决在资源有限的发展中国家，利用传统方法对文化遗产进行3D重建成本高昂、技术门槛高的问题。现有方法，如摄影测量和LiDAR扫描，需要昂贵的设备、专业的操作人员以及大量的现场数据采集，这使得许多珍贵的文化遗产无法被数字化保存。

**核心思路**：论文的核心思路是利用公开可用的谷歌街景图像，结合生成式AI技术，构建一个低成本、易于使用的3D重建框架。通过AI自动分析街景图像，提取建筑物的结构和纹理信息，并生成高质量的3D模型，从而降低了对专业设备和人员的依赖。

**技术框架**：Oitijjo-3D框架包含两个主要阶段：1) **多模态视觉推理与结构-纹理合成**：利用Gemini 2.5 Flash Image模型，分析街景图像，提取建筑物的结构信息和纹理特征，并进行合成，生成高质量的纹理图像。2) **神经图像到3D生成**：使用Hexagen模型，将生成的纹理图像作为输入，重建建筑物的3D几何结构。Hexagen是一个神经渲染模型，能够从单张或少量图像中生成高质量的3D模型。

**关键创新**：该论文的关键创新在于将多模态视觉推理和神经图像到3D生成技术相结合，利用公开的街景图像，实现了快速、低成本的文化遗产3D重建。与传统的运动结构重建（SfM）方法相比，Oitijjo-3D无需大量的图像采集和复杂的后处理，大大降低了时间和成本。

**关键设计**：Gemini 2.5 Flash Image模型用于提取图像中的结构和纹理信息，具体参数设置未知。Hexagen模型使用神经渲染技术，通过优化网络参数，使得生成的3D模型与输入图像在视觉上一致。损失函数的设计未知，但可能包括图像重建损失、几何一致性损失等。具体的网络结构细节未知。

## 📊 实验亮点

Oitijjo-3D在Ahsan Manzil、Choto Sona Mosque和Paharpur等标志性建筑上进行了实验，结果表明该框架能够在几秒钟内生成照片级真实、度量一致的3D模型。与传统的运动结构重建（SfM）流程相比，Oitijjo-3D在速度上实现了显著提升，且无需任何专用硬件或专家监督。具体的性能数据和提升幅度未知。

## 🎯 应用场景

Oitijjo-3D框架可广泛应用于文化遗产保护、虚拟旅游、教育和游戏等领域。它能够帮助资源有限的国家和地区快速数字化其文化遗产，促进文化交流和传承。此外，该技术还可以用于城市规划、建筑设计和灾害评估等领域，具有广阔的应用前景。

## 📄 摘要（原文）

> Cultural heritage restoration in Bangladesh faces a dual challenge of limited resources and scarce technical expertise. Traditional 3D digitization methods, such as photogrammetry or LiDAR scanning, require expensive hardware, expert operators, and extensive on-site access, which are often infeasible in developing contexts. As a result, many of Bangladesh's architectural treasures, from the Paharpur Buddhist Monastery to Ahsan Manzil, remain vulnerable to decay and inaccessible in digital form. This paper introduces Oitijjo-3D, a cost-free generative AI framework that democratizes 3D cultural preservation. By using publicly available Google Street View imagery, Oitijjo-3D reconstructs faithful 3D models of heritage structures through a two-stage pipeline - multimodal visual reasoning with Gemini 2.5 Flash Image for structure-texture synthesis, and neural image-to-3D generation through Hexagen for geometry recovery. The system produces photorealistic, metrically coherent reconstructions in seconds, achieving significant speedups compared to conventional Structure-from-Motion pipelines, without requiring any specialized hardware or expert supervision. Experiments on landmarks such as Ahsan Manzil, Choto Sona Mosque, and Paharpur demonstrate that Oitijjo-3D preserves both visual and structural fidelity while drastically lowering economic and technical barriers. By turning open imagery into digital heritage, this work reframes preservation as a community-driven, AI-assisted act of cultural continuity for resource-limited nations.

