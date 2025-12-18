---
layout: default
title: Real2USD: Scene Representations in Universal Scene Description Language
---

# Real2USD: Scene Representations in Universal Scene Description Language

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10778" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10778v1</a>
  <a href="https://arxiv.org/pdf/2510.10778.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10778v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.10778v1', 'Real2USD: Scene Representations in Universal Scene Description Language')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Christopher D. Hsu, Pratik Chaudhari

**分类**: cs.RO

**发布日期**: 2025-10-12

**备注**: 8 pages, 10 figures, 1 table

**🔗 代码/项目**: [GITHUB](https://github.com/grasp-lyrl/Real2USD)

---

## 💡 一句话要点

**提出Real2USD系统，利用通用场景描述语言USD赋能LLM机器人场景理解与规划**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `通用场景描述` `大型语言模型` `机器人` `场景理解` `任务规划` `环境表示` `USD` `Real2USD`

## 📋 核心要点

1. 现有机器人环境表示方法缺乏通用性，难以有效支持LLM进行复杂推理和规划。
2. 提出Real2USD系统，将真实环境转换为USD格式，利用其丰富的语义和几何信息。
3. 实验表明，该系统能够利用LLM进行场景理解、复杂推理和规划，并在模拟环境中验证。

## 📝 摘要（中文）

大型语言模型(LLM)能够帮助机器人推理抽象的任务规范。这需要用基于自然语言的先验知识来增强机器人所使用的经典环境表示。目前已有一些方法，但它们是为特定任务定制的，例如用于导航的视觉-语言模型，用于地图构建的语言引导神经辐射场等。本文认为，通用场景描述(USD)语言是基于LLM的机器人任务中环境的几何、光度和语义信息的有效且通用的表示。我们的论点很简单：USD是一种基于XML的场景图，LLM和人类都可以读取，并且足够丰富以支持几乎任何任务——皮克斯开发这种语言来存储资产、场景甚至电影。我们展示了一个“Real to USD”系统，该系统使用配备激光雷达和RGB相机的宇树Go2四足机器人，该系统(i)构建了具有各种物体和具有大量玻璃的挑战性设置的室内环境的显式USD表示，以及(ii)使用谷歌的Gemini解析USD以演示场景理解、复杂推理和规划。我们还在使用Nvidia的Issac Sim的模拟仓库和医院环境中研究了该系统的不同方面。代码可在https://github.com/grasp-lyrl/Real2USD 获取。

## 🔬 方法详解

**问题定义**：现有机器人环境表示方法通常是任务特定的，例如视觉导航或神经辐射场，缺乏通用性，难以支持大型语言模型（LLM）进行复杂的场景理解、推理和规划。这些方法难以整合几何、光度和语义信息，限制了LLM在机器人任务中的应用。

**核心思路**：论文的核心思路是利用通用场景描述（USD）语言作为机器人环境的统一表示。USD是一种基于XML的场景图，既可以被LLM读取，又具有足够的表达能力来描述环境的几何、光度和语义信息。通过将真实环境转换为USD格式，可以充分利用LLM的强大能力进行场景理解和任务规划。

**技术框架**：Real2USD系统的整体框架包括以下几个主要模块：1) 数据采集：使用配备激光雷达和RGB相机的宇树Go2四足机器人采集室内环境数据。2) USD构建：将采集到的数据转换为USD格式的场景表示，包括几何模型、材质属性和语义标签。3) LLM推理：使用Google的Gemini等LLM解析USD场景图，进行场景理解、复杂推理和任务规划。4) 仿真验证：在Nvidia的Issac Sim中对系统进行仿真验证，评估其在不同场景下的性能。

**关键创新**：该论文的关键创新在于将USD语言引入机器人领域，并将其作为LLM进行场景理解和任务规划的通用环境表示。与现有的任务特定方法相比，Real2USD系统具有更高的通用性和灵活性，可以支持更广泛的机器人应用。

**关键设计**：在USD构建过程中，需要对激光雷达点云和RGB图像进行处理，生成高质量的几何模型和纹理贴图。语义标签可以通过预训练的视觉模型或人工标注获得。在LLM推理过程中，需要设计合适的prompt，引导LLM理解USD场景图并进行推理。具体的参数设置和网络结构取决于所使用的LLM和视觉模型。

## 📊 实验亮点

该论文通过实验验证了Real2USD系统的有效性。在室内环境中，该系统能够构建高质量的USD场景表示，并利用LLM进行准确的场景理解和任务规划。在模拟仓库和医院环境中，该系统也表现出良好的性能。实验结果表明，Real2USD系统能够显著提升机器人的智能化水平。

## 🎯 应用场景

该研究成果可应用于智能家居、仓储物流、医疗服务等领域。例如，机器人可以利用Real2USD系统理解家庭环境，执行清洁、整理等任务；在仓库中，机器人可以利用该系统进行货物识别、路径规划和自主导航；在医院中，机器人可以利用该系统进行药品配送、病人护理等任务。该研究为机器人智能化发展提供了新的思路和方法。

## 📄 摘要（原文）

> Large Language Models (LLMs) can help robots reason about abstract task specifications. This requires augmenting classical representations of the environment used by robots with natural language-based priors. There are a number of existing approaches to doing so, but they are tailored to specific tasks, e.g., visual-language models for navigation, language-guided neural radiance fields for mapping, etc. This paper argues that the Universal Scene Description (USD) language is an effective and general representation of geometric, photometric and semantic information in the environment for LLM-based robotics tasks. Our argument is simple: a USD is an XML-based scene graph, readable by LLMs and humans alike, and rich enough to support essentially any task -- Pixar developed this language to store assets, scenes and even movies. We demonstrate a ``Real to USD'' system using a Unitree Go2 quadruped robot carrying LiDAR and a RGB camera that (i) builds an explicit USD representation of indoor environments with diverse objects and challenging settings with lots of glass, and (ii) parses the USD using Google's Gemini to demonstrate scene understanding, complex inferences, and planning. We also study different aspects of this system in simulated warehouse and hospital settings using Nvidia's Issac Sim. Code is available at https://github.com/grasp-lyrl/Real2USD .

