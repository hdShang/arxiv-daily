---
layout: default
title: Bridging Perception and Reasoning: Dual-Pipeline Neuro-Symbolic Landing for UAVs in Cluttered Environments
---

# Bridging Perception and Reasoning: Dual-Pipeline Neuro-Symbolic Landing for UAVs in Cluttered Environments

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.22204" target="_blank" class="toolbar-btn">arXiv: 2510.22204v1</a>
    <a href="https://arxiv.org/pdf/2510.22204.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22204v1" 
            onclick="toggleFavorite(this, '2510.22204v1', 'Bridging Perception and Reasoning: Dual-Pipeline Neuro-Symbolic Landing for UAVs in Cluttered Environments')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Weixian Qian, Sebastian Schroder, Yao Deng, Jiaohong Yao, Linfeng Liang, Xiao Cheng, Richard Han, Xi Zheng

**分类**: cs.RO, cs.AI

**发布日期**: 2025-10-25

---

## 💡 一句话要点

**NeuroSymLand：结合神经符号推理，提升无人机在复杂环境下的自主着陆能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无人机自主着陆` `神经符号推理` `语义分割` `大型语言模型` `知识表示` `演绎推理` `非结构化环境`

## 📋 核心要点

1. 现有无人机自主着陆方法在复杂环境下表现不佳，纯视觉或深度学习模型泛化能力有限，缺乏可解释性。
2. NeuroSymLand结合神经感知和符号推理，利用LLM生成可验证的Scallop代码，并使用轻量级基础模型进行实时推理。
3. 实验结果表明，NeuroSymLand在准确率、鲁棒性和效率方面优于现有方法，提升了无人机着陆的安全性和可靠性。

## 📝 摘要（中文）

本文提出NeuroSymLand，一种神经符号框架，用于提升无人机在非结构化环境（杂乱、不平坦、缺乏地图信息）下的自主着陆能力。该框架紧密耦合两个互补的流程：（1）离线流程，利用大型语言模型（LLMs）和人机协作，从各种着陆场景中合成Scallop代码，提炼通用且可验证的符号知识；（2）在线流程，利用轻量级的基础模型进行语义分割，生成概率性的Scallop事实，并将其组合成语义场景图，用于实时演绎推理。这种设计结合了轻量级基础模型的感知能力与符号推理的可解释性和可验证性。节点属性（如平坦度、面积）和边关系（邻接、包含、邻近）通过几何例程计算，而非学习得到，避免了训练时图构建器的数据依赖性和延迟。生成的Scallop程序编码了着陆原则（避开水域和障碍物；偏好大型、平坦、可达的区域），并产生校准后的安全评分，以及排序后的感兴趣区域（ROIs）和人类可读的理由。在数据集、多样化的模拟地图和真实无人机硬件上的大量评估表明，NeuroSymLand相比最先进的基线方法，实现了更高的准确率、更强的协变量偏移鲁棒性和更优越的效率，同时提高了无人机在应急响应、监视和交付任务中的安全性和可靠性。

## 🔬 方法详解

**问题定义**：无人机在非结构化环境中自主着陆是一个具有挑战性的问题。现有的纯视觉或深度学习方法在面对环境变化时，泛化能力较弱，容易出现错误，并且缺乏可解释性，难以保证安全性。这些方法通常依赖大量数据进行训练，并且难以处理未知的环境条件。

**核心思路**：NeuroSymLand的核心思路是将神经感知和符号推理相结合，利用深度学习模型进行环境感知，提取语义信息，然后利用符号推理进行决策，生成可解释的着陆方案。这种方法结合了深度学习的感知能力和符号推理的可解释性和可验证性，从而提高了无人机在复杂环境下的自主着陆能力。

**技术框架**：NeuroSymLand包含两个主要流程：离线流程和在线流程。离线流程利用大型语言模型（LLMs）和人机协作，从各种着陆场景中合成Scallop代码，提炼通用且可验证的符号知识。在线流程利用轻量级的基础模型进行语义分割，生成概率性的Scallop事实，并将其组合成语义场景图，用于实时演绎推理。两个流程紧密耦合，共同完成无人机的自主着陆任务。

**关键创新**：NeuroSymLand的关键创新在于将神经感知和符号推理紧密结合，利用LLM生成可验证的Scallop代码，并使用轻量级基础模型进行实时推理。此外，该方法使用几何例程计算节点属性和边关系，避免了训练时图构建器的数据依赖性和延迟。这种设计提高了无人机在复杂环境下的自主着陆能力，并保证了安全性和可靠性。

**关键设计**：NeuroSymLand的关键设计包括：(1) 使用LLM生成Scallop代码，编码着陆原则；(2) 使用轻量级基础模型进行语义分割，生成概率性的Scallop事实；(3) 使用几何例程计算节点属性和边关系；(4) 使用Scallop程序进行演绎推理，生成校准后的安全评分和排序后的感兴趣区域（ROIs）。这些设计共同保证了NeuroSymLand的准确性、鲁棒性和效率。

## 📊 实验亮点

实验结果表明，NeuroSymLand在数据集、多样化的模拟地图和真实无人机硬件上的大量评估中，相比最先进的基线方法，实现了更高的准确率、更强的协变量偏移鲁棒性和更优越的效率。具体性能数据和提升幅度在论文中有详细展示，证明了NeuroSymLand的有效性。

## 🎯 应用场景

NeuroSymLand可应用于应急响应、监视和交付等领域。在应急响应中，无人机可以自主着陆在复杂环境中，快速到达救援现场。在监视任务中，无人机可以自主选择安全的着陆点，进行长时间的监视。在交付任务中，无人机可以自主着陆在用户指定的地点，完成包裹的交付。该研究成果有助于提高无人机在各种实际应用中的安全性和可靠性。

## 📄 摘要（原文）

> Autonomous landing in unstructured (cluttered, uneven, and map-poor) environments is a core requirement for Unmanned Aerial Vehicles (UAVs), yet purely vision-based or deep learning models often falter under covariate shift and provide limited interpretability. We propose NeuroSymLand, a neuro-symbolic framework that tightly couples two complementary pipelines: (i) an offline pipeline, where Large Language Models (LLMs) and human-in-the-loop refinement synthesize Scallop code from diverse landing scenarios, distilling generalizable and verifiable symbolic knowledge; and (ii) an online pipeline, where a compact foundation-based semantic segmentation model generates probabilistic Scallop facts that are composed into semantic scene graphs for real-time deductive reasoning. This design combines the perceptual strengths of lightweight foundation models with the interpretability and verifiability of symbolic reasoning. Node attributes (e.g., flatness, area) and edge relations (adjacency, containment, proximity) are computed with geometric routines rather than learned, avoiding the data dependence and latency of train-time graph builders. The resulting Scallop program encodes landing principles (avoid water and obstacles; prefer large, flat, accessible regions) and yields calibrated safety scores with ranked Regions of Interest (ROIs) and human-readable justifications. Extensive evaluations across datasets, diverse simulation maps, and real UAV hardware show that NeuroSymLand achieves higher accuracy, stronger robustness to covariate shift, and superior efficiency compared with state-of-the-art baselines, while advancing UAV safety and reliability in emergency response, surveillance, and delivery missions.

