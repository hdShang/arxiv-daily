---
layout: default
title: "CAMS: A CityGPT-Powered Agentic Framework for Urban Human Mobility Simulation"
---

# CAMS: A CityGPT-Powered Agentic Framework for Urban Human Mobility Simulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13599" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13599v1</a>
  <a href="https://arxiv.org/pdf/2506.13599.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13599v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13599v1', 'CAMS: A CityGPT-Powered Agentic Framework for Urban Human Mobility Simulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuwei Du, Jie Feng, Jian Yuan, Yong Li

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-16

---

## 💡 一句话要点

**提出CAMS框架以解决城市人类移动模拟中的数据驱动不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人类移动模拟` `城市规划` `大型语言模型` `代理框架` `轨迹生成` `数据驱动方法` `智能城市`

## 📋 核心要点

1. 现有方法在城市人类移动模拟中面临建模不足和个体与集体移动模式整合不良的挑战。
2. CAMS框架通过结合语言基础模型和代理机制，全面模拟城市空间中的人类移动。
3. 实验结果显示，CAMS在真实数据集上表现优越，生成的轨迹更具现实性和可信度。

## 📝 摘要（中文）

人类移动模拟在多种现实应用中至关重要。为了解决传统数据驱动方法的局限性，研究者们开始探索利用大型语言模型的常识知识和推理能力来加速人类移动模拟。然而，这些方法存在城市空间建模不足和个体与集体移动模式整合不良等关键问题。为此，本文提出了城市GPT驱动的代理框架CAMS，该框架利用基于语言的城市基础模型在城市空间中模拟人类移动。CAMS包括三个核心模块：MobExtractor用于提取模板移动模式并基于用户画像合成新模式；GeoGenerator考虑集体知识生成锚点并使用增强版CityGPT生成候选城市地理空间知识；TrajEnhancer基于移动模式检索空间知识并通过DPO生成与真实轨迹偏好对齐的轨迹。实验证明，CAMS在不依赖外部地理空间信息的情况下，表现优越，生成更真实的轨迹。

## 🔬 方法详解

**问题定义**：本文旨在解决传统人类移动模拟方法在城市空间建模和个体与集体移动模式整合方面的不足，导致生成的轨迹不够真实和可信。

**核心思路**：CAMS框架通过引入大型语言模型的推理能力，结合代理机制，全面模拟城市中的人类移动，旨在提高模拟的准确性和现实性。

**技术框架**：CAMS框架由三个主要模块组成：MobExtractor用于提取和合成移动模式；GeoGenerator生成锚点和城市地理空间知识；TrajEnhancer基于移动模式生成与真实轨迹偏好一致的轨迹。

**关键创新**：CAMS的核心创新在于将语言模型与代理框架结合，全面考虑个体和集体移动模式，从而生成更为真实的轨迹，这一方法与传统的单一数据驱动方法有本质区别。

**关键设计**：在MobExtractor中，使用用户画像来合成新移动模式；GeoGenerator采用增强版CityGPT生成城市知识；TrajEnhancer通过DPO对生成轨迹进行优化，以确保与真实轨迹偏好对齐。

## 📊 实验亮点

实验结果表明，CAMS在真实数据集上的表现显著优于传统方法，生成的轨迹在真实性和可信度上有明显提升，具体性能数据未提供，但整体效果显著改善。

## 🎯 应用场景

CAMS框架在城市规划、交通管理和智能城市建设等领域具有广泛的应用潜力。通过更准确的人类移动模拟，相关部门可以优化交通流量、提升公共服务效率，并为未来城市发展提供数据支持。

## 📄 摘要（原文）

> Human mobility simulation plays a crucial role in various real-world applications. Recently, to address the limitations of traditional data-driven approaches, researchers have explored leveraging the commonsense knowledge and reasoning capabilities of large language models (LLMs) to accelerate human mobility simulation. However, these methods suffer from several critical shortcomings, including inadequate modeling of urban spaces and poor integration with both individual mobility patterns and collective mobility distributions. To address these challenges, we propose \textbf{C}ityGPT-Powered \textbf{A}gentic framework for \textbf{M}obility \textbf{S}imulation (\textbf{CAMS}), an agentic framework that leverages the language based urban foundation model to simulate human mobility in urban space. \textbf{CAMS} comprises three core modules, including MobExtractor to extract template mobility patterns and synthesize new ones based on user profiles, GeoGenerator to generate anchor points considering collective knowledge and generate candidate urban geospatial knowledge using an enhanced version of CityGPT, TrajEnhancer to retrieve spatial knowledge based on mobility patterns and generate trajectories with real trajectory preference alignment via DPO. Experiments on real-world datasets show that \textbf{CAMS} achieves superior performance without relying on externally provided geospatial information. Moreover, by holistically modeling both individual mobility patterns and collective mobility constraints, \textbf{CAMS} generates more realistic and plausible trajectories. In general, \textbf{CAMS} establishes a new paradigm that integrates the agentic framework with urban-knowledgeable LLMs for human mobility simulation.

