---
layout: default
title: All You Need for Object Detection: From Pixels, Points, and Prompts to Next-Gen Fusion and Multimodal LLMs/VLMs in Autonomous Vehicles
---

# All You Need for Object Detection: From Pixels, Points, and Prompts to Next-Gen Fusion and Multimodal LLMs/VLMs in Autonomous Vehicles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.26641" class="toolbar-btn" target="_blank">📄 arXiv: 2510.26641v2</a>
  <a href="https://arxiv.org/pdf/2510.26641.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.26641v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.26641v2', 'All You Need for Object Detection: From Pixels, Points, and Prompts to Next-Gen Fusion and Multimodal LLMs/VLMs in Autonomous Vehicles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sayed Pedram Haeri Boroujeni, Niloufar Mehrabi, Hazim Alzorgan, Mahlagha Fazeli, Abolfazl Razi

**分类**: cs.CV

**发布日期**: 2025-10-30 (更新: 2025-12-02)

---

## 💡 一句话要点

**面向自动驾驶，综述融合LLM/VLM的新一代多模态目标检测技术**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `目标检测` `多模态融合` `视觉语言模型` `大型语言模型` `传感器融合` `Transformer` `协同感知`

## 📋 核心要点

1. 现有自动驾驶目标检测方法在多模态感知、上下文推理和协同智能方面存在知识碎片化的问题，限制了其性能。
2. 该综述着重分析了视觉语言模型（VLMs）、大型语言模型（LLMs）和生成式AI等新兴技术在自动驾驶目标检测中的应用。
3. 论文系统回顾了各种传感器及其融合策略，并对现有数据集进行了结构化分类和交叉分析，为未来研究提供了清晰的路线图。

## 📝 摘要（中文）

自动驾驶汽车（AVs）正通过智能感知、决策和控制系统的进步改变交通运输的未来。然而，它们的成功与一项核心能力息息相关，即在复杂和多模态环境中可靠的目标检测。尽管计算机视觉（CV）和人工智能（AI）的最新突破推动了显著的进展，但该领域仍然面临着一个关键挑战，即知识仍然分散在多模态感知、上下文推理和协同智能中。本综述通过对AV中目标检测的前瞻性分析来弥合这一差距，强调诸如视觉语言模型（VLMs）、大型语言模型（LLMs）和生成式AI等新兴范式，而不是重新审视过时的技术。我们首先系统地回顾了AV传感器的基本频谱（摄像头、超声波、激光雷达和雷达）及其融合策略，不仅强调了它们在动态驾驶环境中的能力和局限性，还强调了它们与LLM/VLM驱动的感知框架集成的潜力。接下来，我们介绍了一种结构化的AV数据集分类，它超越了简单的数据集合，定位了自我车辆、基于基础设施和协同数据集（例如，V2V、V2I、V2X、I2I），然后对数据结构和特征进行交叉分析。最后，我们分析了最先进的检测方法，从2D和3D流水线到混合传感器融合，特别关注由视觉Transformer（ViTs）、大型和小型语言模型（SLMs）以及VLM驱动的新兴Transformer驱动方法。通过综合这些观点，我们的综述提供了一个关于当前能力、开放挑战和未来机遇的清晰路线图。

## 🔬 方法详解

**问题定义**：自动驾驶车辆需要在复杂和多变的环境中进行可靠的目标检测，而现有的方法往往侧重于单一模态或简单的传感器融合，缺乏对上下文信息的有效利用和协同感知能力。此外，知识碎片化也阻碍了该领域的发展。

**核心思路**：本综述的核心思路是分析和整合近年来在计算机视觉和自然语言处理领域取得的最新进展，特别是视觉语言模型（VLMs）和大型语言模型（LLMs），并将其应用于自动驾驶目标检测任务中。通过利用LLM/VLM强大的语义理解和推理能力，可以更好地理解场景上下文，提高目标检测的准确性和鲁棒性。

**技术框架**：该综述首先回顾了自动驾驶车辆常用的传感器类型（摄像头、激光雷达、毫米波雷达、超声波雷达）及其融合策略，分析了它们的优缺点和适用场景。然后，对现有的自动驾驶数据集进行了分类和分析，包括自车数据集、基础设施数据集和协同数据集。最后，重点介绍了基于Transformer的检测方法，包括ViT、LLM/SLM和VLM，并分析了它们在2D、3D和多模态目标检测中的应用。

**关键创新**：该综述的关键创新在于它将LLM/VLM等新兴技术引入到自动驾驶目标检测领域，并系统地分析了它们的应用前景和挑战。与传统的基于规则或手工特征的方法相比，LLM/VLM能够更好地理解场景上下文，提高目标检测的泛化能力和鲁棒性。

**关键设计**：该综述并没有提出具体的算法或模型，而是对现有方法进行了梳理和总结，并指出了未来的研究方向。例如，如何设计更有效的LLM/VLM模型来处理自动驾驶场景中的复杂数据，如何将LLM/VLM与传统的传感器融合方法相结合，以及如何利用协同感知技术来提高目标检测的准确性和可靠性。

## 📊 实验亮点

该综述系统地回顾了自动驾驶目标检测领域的最新进展，并重点分析了LLM/VLM等新兴技术的应用前景。通过对现有数据集的分类和分析，为未来的研究提供了参考。该综述还指出了当前研究面临的挑战和未来的研究方向，为该领域的发展提供了指导。

## 🎯 应用场景

该研究成果对自动驾驶领域具有重要的应用价值。通过融合LLM/VLM等技术，可以提高自动驾驶车辆在复杂环境下的感知能力，从而提高驾驶安全性。此外，该研究还可以应用于智能交通系统、机器人等领域，促进人工智能技术的发展。

## 📄 摘要（原文）

> Autonomous Vehicles (AVs) are transforming the future of transportation through advances in intelligent perception, decision-making, and control systems. However, their success is tied to one core capability, reliable object detection in complex and multimodal environments. While recent breakthroughs in Computer Vision (CV) and Artificial Intelligence (AI) have driven remarkable progress, the field still faces a critical challenge as knowledge remains fragmented across multimodal perception, contextual reasoning, and cooperative intelligence. This survey bridges that gap by delivering a forward-looking analysis of object detection in AVs, emphasizing emerging paradigms such as Vision-Language Models (VLMs), Large Language Models (LLMs), and Generative AI rather than re-examining outdated techniques. We begin by systematically reviewing the fundamental spectrum of AV sensors (camera, ultrasonic, LiDAR, and Radar) and their fusion strategies, highlighting not only their capabilities and limitations in dynamic driving environments but also their potential to integrate with recent advances in LLM/VLM-driven perception frameworks. Next, we introduce a structured categorization of AV datasets that moves beyond simple collections, positioning ego-vehicle, infrastructure-based, and cooperative datasets (e.g., V2V, V2I, V2X, I2I), followed by a cross-analysis of data structures and characteristics. Ultimately, we analyze cutting-edge detection methodologies, ranging from 2D and 3D pipelines to hybrid sensor fusion, with particular attention to emerging transformer-driven approaches powered by Vision Transformers (ViTs), Large and Small Language Models (SLMs), and VLMs. By synthesizing these perspectives, our survey delivers a clear roadmap of current capabilities, open challenges, and future opportunities.

