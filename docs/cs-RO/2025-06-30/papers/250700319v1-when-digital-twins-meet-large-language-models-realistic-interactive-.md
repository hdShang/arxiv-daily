---
layout: default
title: "When Digital Twins Meet Large Language Models: Realistic, Interactive, and Editable Simulation for Autonomous Driving"
---

# When Digital Twins Meet Large Language Models: Realistic, Interactive, and Editable Simulation for Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00319" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00319v1</a>
  <a href="https://arxiv.org/pdf/2507.00319.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00319v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00319v1', 'When Digital Twins Meet Large Language Models: Realistic, Interactive, and Editable Simulation for Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tanmay Vilas Samak, Chinmay Vilas Samak, Bing Li, Venkat Krovi

**分类**: cs.RO

**发布日期**: 2025-06-30

---

## 💡 一句话要点

**提出统一框架以解决自主驾驶仿真中的多重挑战**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数字双胞胎` `自主驾驶` `仿真框架` `自然语言处理` `实时性能` `物理仿真` `数据驱动技术`

## 📋 核心要点

1. 现有的自主驾驶仿真方法在动态真实感、光线真实渲染等方面难以兼顾，导致无法满足高保真仿真的需求。
2. 本文提出了一种统一的框架，通过结合物理和数据驱动技术，创建高保真的数字双胞胎，以提升自主驾驶仿真的质量和效率。
3. 实验结果显示，该框架在3D场景重建中实现了97%的结构相似度，帧率超过60 Hz，且能够生成高重复性和泛化能力的驾驶场景。

## 📝 摘要（中文）

仿真框架是自主驾驶系统开发与验证的重要工具。然而，现有方法在动态真实感、光线真实渲染、场景编排和实时性能等方面存在不足。为此，本文提出了一种统一框架，旨在创建和管理高保真数字双胞胎，以加速自主驾驶研究的进展。该框架结合了基于物理和数据驱动的技术，能够以几何和光线真实的准确性重建现实世界场景，并赋予其各种物理属性，实现实时动态仿真。此外，框架还集成了大型语言模型接口，允许用户通过自然语言提示在线灵活编辑驾驶场景。实验结果表明，该框架能够以高达97%的结构相似度重建3D场景，并保持超过60 Hz的帧率，同时生成多样化的驾驶场景，重复性高达95%，泛化能力达到85%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自主驾驶仿真方法在动态真实感、光线真实渲染、场景编排和实时性能等方面的不足，导致无法全面满足自主驾驶系统的需求。

**核心思路**：提出一种统一框架，结合物理基础和数据驱动技术，创建高保真的数字双胞胎，能够准确重建现实世界场景并实现实时动态仿真，同时通过大型语言模型接口支持自然语言场景编辑。

**技术框架**：该框架包括多个主要模块：1) 现实场景重建模块，负责从真实世界获取数据并重建3D场景；2) 动态仿真模块，赋予场景物理属性以实现实时仿真；3) 语言模型接口，支持用户通过自然语言编辑场景。

**关键创新**：最重要的创新在于将大型语言模型与数字双胞胎技术结合，使得用户能够通过自然语言灵活编辑仿真场景，这在现有方法中是前所未有的。

**关键设计**：在技术细节上，框架采用了高效的几何重建算法和物理引擎，确保了场景重建的准确性和实时性，同时优化了语言模型的提示处理能力，以提高场景生成的多样性和准确性。

## 📊 实验亮点

实验结果表明，框架在3D场景重建中实现了高达97%的结构相似度，且帧率保持在60 Hz以上。此外，框架能够处理自然语言提示，生成多样化的驾驶场景，重复性高达95%，泛化能力达到85%，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶汽车的开发与测试、智能交通系统的仿真以及城市规划等。通过提供高保真的仿真环境，能够有效加速自主驾驶技术的验证与部署，提升安全性和效率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Simulation frameworks have been key enablers for the development and validation of autonomous driving systems. However, existing methods struggle to comprehensively address the autonomy-oriented requirements of balancing: (i) dynamical fidelity, (ii) photorealistic rendering, (iii) context-relevant scenario orchestration, and (iv) real-time performance. To address these limitations, we present a unified framework for creating and curating high-fidelity digital twins to accelerate advancements in autonomous driving research. Our framework leverages a mix of physics-based and data-driven techniques for developing and simulating digital twins of autonomous vehicles and their operating environments. It is capable of reconstructing real-world scenes and assets (real2sim) with geometric and photorealistic accuracy and infusing them with various physical properties to enable real-time dynamical simulation of the ensuing driving scenarios. Additionally, it also incorporates a large language model (LLM) interface to flexibly edit the driving scenarios online via natural language prompts. We analyze the presented framework in terms of its fidelity, performance, and serviceability. Results indicate that our framework can reconstruct 3D scenes and assets with up to 97% structural similarity, while maintaining frame rates above 60 Hz. We also demonstrate that it can handle natural language prompts to generate diverse driving scenarios with up to 95% repeatability and 85% generalizability.

