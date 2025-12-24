---
layout: default
title: "GeoProg3D: Compositional Visual Reasoning for City-Scale 3D Language Fields"
---

# GeoProg3D: Compositional Visual Reasoning for City-Scale 3D Language Fields

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23352" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23352v1</a>
  <a href="https://arxiv.org/pdf/2506.23352.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23352v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23352v1', 'GeoProg3D: Compositional Visual Reasoning for City-Scale 3D Language Fields')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shunsuke Yasuki, Taiki Miyanishi, Nakamasa Inoue, Shuhei Kurita, Koya Sakamoto, Daichi Azuma, Masato Taki, Yutaka Matsuo

**分类**: cs.CV

**发布日期**: 2025-06-29

**备注**: Accepted by ICCV 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://snskysk.github.io/GeoProg3D/)

---

## 💡 一句话要点

**提出GeoProg3D以解决城市规模3D语言场景交互问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D语言处理` `城市规模` `自然语言交互` `地理信息` `视觉编程` `大语言模型` `组合推理`

## 📋 核心要点

1. 现有3D语言处理方法通常只能在小规模环境中有效工作，缺乏处理复杂城市场景的能力。
2. GeoProg3D通过引入地理感知的3D语言场和地理视觉API，提供了一种新的自然语言交互框架，支持城市规模的高保真3D场景。
3. 实验结果表明，GeoProg3D在多个推理任务上显著优于现有模型，展示了其在城市规模3D环境中的有效性。

## 📝 摘要（中文）

随着3D语言领域的发展，用户可以通过自然语言与3D场景进行直观交互。然而，现有方法通常局限于小规模环境，缺乏在复杂城市环境中所需的可扩展性和组合推理能力。为此，本文提出了GeoProg3D，一个视觉编程框架，支持与城市规模高保真3D场景的自然语言驱动交互。GeoProg3D包含两个关键组件：地理感知城市规模3D语言场（GCLF）和地理视觉API（GV-APIs）。通过大语言模型（LLMs）作为推理引擎，GeoProg3D在多个任务中显著超越现有3D语言场和视觉-语言模型，首次实现了高保真城市规模3D环境中的组合地理推理。

## 🔬 方法详解

**问题定义**：本文旨在解决现有3D语言处理方法在城市规模复杂环境中的局限性，尤其是在可扩展性和组合推理能力方面的不足。

**核心思路**：GeoProg3D的核心思路是结合地理信息和高效的3D模型，通过自然语言实现对城市规模3D场景的交互，利用大语言模型进行动态推理。

**技术框架**：GeoProg3D框架主要由两个组件构成：地理感知城市规模3D语言场（GCLF）和地理视觉API（GV-APIs）。GCLF通过分层3D模型处理大规模数据，GV-APIs则提供区域分割和物体检测等工具。

**关键创新**：GeoProg3D首次实现了在高保真城市规模3D环境中通过自然语言进行组合地理推理的能力，这一创新显著提升了交互的灵活性和准确性。

**关键设计**：在设计上，GeoProg3D采用了内存高效的分层3D模型，并结合地理信息进行数据过滤，使用大语言模型作为推理引擎，确保了系统的高效性和准确性。

## 📊 实验亮点

实验结果显示，GeoProg3D在952个查询-回答对的评估中，针对基础的地面定位、空间推理、比较、计数和测量等五个任务，显著超越了现有的3D语言场和视觉-语言模型，展示了其在城市规模推理中的卓越性能。

## 🎯 应用场景

GeoProg3D的潜在应用场景包括城市规划、智能导航、虚拟现实和增强现实等领域。通过自然语言与复杂3D环境的交互，用户可以更直观地获取信息，提升决策效率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The advancement of 3D language fields has enabled intuitive interactions with 3D scenes via natural language. However, existing approaches are typically limited to small-scale environments, lacking the scalability and compositional reasoning capabilities necessary for large, complex urban settings. To overcome these limitations, we propose GeoProg3D, a visual programming framework that enables natural language-driven interactions with city-scale high-fidelity 3D scenes. GeoProg3D consists of two key components: (i) a Geography-aware City-scale 3D Language Field (GCLF) that leverages a memory-efficient hierarchical 3D model to handle large-scale data, integrated with geographic information for efficiently filtering vast urban spaces using directional cues, distance measurements, elevation data, and landmark references; and (ii) Geographical Vision APIs (GV-APIs), specialized geographic vision tools such as area segmentation and object detection. Our framework employs large language models (LLMs) as reasoning engines to dynamically combine GV-APIs and operate GCLF, effectively supporting diverse geographic vision tasks. To assess performance in city-scale reasoning, we introduce GeoEval3D, a comprehensive benchmark dataset containing 952 query-answer pairs across five challenging tasks: grounding, spatial reasoning, comparison, counting, and measurement. Experiments demonstrate that GeoProg3D significantly outperforms existing 3D language fields and vision-language models across multiple tasks. To our knowledge, GeoProg3D is the first framework enabling compositional geographic reasoning in high-fidelity city-scale 3D environments via natural language. The code is available at https://snskysk.github.io/GeoProg3D/.

