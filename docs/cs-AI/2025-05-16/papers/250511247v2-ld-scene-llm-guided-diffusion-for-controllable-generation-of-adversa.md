---
layout: default
title: LD-Scene: LLM-Guided Diffusion for Controllable Generation of Adversarial Safety-Critical Driving Scenarios
---

# LD-Scene: LLM-Guided Diffusion for Controllable Generation of Adversarial Safety-Critical Driving Scenarios

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11247" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11247v2</a>
  <a href="https://arxiv.org/pdf/2505.11247.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11247v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11247v2', 'LD-Scene: LLM-Guided Diffusion for Controllable Generation of Adversarial Safety-Critical Driving Scenarios')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingxing Peng, Yuting Xie, Xusen Guo, Ruoyu Yao, Hai Yang, Jun Ma

**分类**: cs.AI, cs.LG, cs.RO

**发布日期**: 2025-05-16 (更新: 2025-08-17)

**备注**: 18 pages, 8 figures

---

## 💡 一句话要点

**提出LD-Scene以解决自动驾驶安全场景生成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `对抗场景生成` `安全测试` `大型语言模型` `潜在扩散模型` `用户可控性` `鲁棒性`

## 📋 核心要点

1. 现有方法在生成安全关键驾驶场景时缺乏可控性和用户友好性，且需要大量专家知识。
2. LD-Scene框架结合了大型语言模型和潜在扩散模型，通过自然语言实现对抗场景的用户控制生成。
3. 在nuScenes数据集上的实验表明，LD-Scene在生成对抗场景的真实性和多样性方面达到了最先进的性能。

## 📝 摘要（中文）

确保自动驾驶系统的安全性和鲁棒性需要在安全关键场景中进行全面评估。然而，这些场景在现实世界中稀缺且难以收集，给评估自动驾驶车辆的性能带来了重大挑战。现有方法通常缺乏可控性和用户友好性，因为需要大量专业知识。为了解决这些挑战，我们提出了LD-Scene，一个将大型语言模型（LLMs）与潜在扩散模型（LDMs）结合的框架，通过自然语言实现用户可控的对抗场景生成。该方法包括一个捕捉真实驾驶轨迹分布的LDM和一个将用户查询转化为对抗损失函数的LLM指导模块。通过在nuScenes数据集上的广泛实验，LD-Scene在生成真实、多样且有效的对抗场景方面达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本论文旨在解决自动驾驶系统在安全关键场景生成中的可控性不足和数据稀缺问题。现有方法通常需要大量的专家知识，导致用户难以有效生成所需的对抗场景。

**核心思路**：LD-Scene通过将大型语言模型与潜在扩散模型结合，允许用户通过自然语言描述生成对抗场景，从而提升生成过程的可控性和灵活性。

**技术框架**：该框架主要包括两个模块：潜在扩散模型（LDM），用于捕捉真实的驾驶轨迹分布；以及LLM指导模块，将用户的自然语言查询转化为对抗损失函数，指导场景生成。

**关键创新**：LD-Scene的创新在于将LLM与LDM结合，利用LLM的推理能力生成对抗场景的指导函数，显著提升了场景生成的可控性和多样性。

**关键设计**：在设计中，LLM指导模块包括链式思维（CoT）代码生成器和代码调试器，增强了生成过程的鲁棒性。损失函数的设计也经过精心调整，以确保生成场景的有效性和多样性。

## 📊 实验亮点

LD-Scene在nuScenes数据集上的实验结果显示，其生成的对抗场景在真实性和多样性方面达到了最先进的性能，相较于现有方法，生成效果提升显著，具体性能数据未提供，但实验结果表明其有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶系统的安全测试、对抗场景的生成与评估，以及智能交通系统的优化。通过提供可控的对抗场景生成，LD-Scene能够帮助研究人员和工程师更有效地测试和提升自动驾驶技术的安全性与可靠性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Ensuring the safety and robustness of autonomous driving systems necessitates a comprehensive evaluation in safety-critical scenarios. However, these safety-critical scenarios are rare and difficult to collect from real-world driving data, posing significant challenges to effectively assessing the performance of autonomous vehicles. Typical existing methods often suffer from limited controllability and lack user-friendliness, as extensive expert knowledge is essentially required. To address these challenges, we propose LD-Scene, a novel framework that integrates Large Language Models (LLMs) with Latent Diffusion Models (LDMs) for user-controllable adversarial scenario generation through natural language. Our approach comprises an LDM that captures realistic driving trajectory distributions and an LLM-based guidance module that translates user queries into adversarial loss functions, facilitating the generation of scenarios aligned with user queries. The guidance module integrates an LLM-based Chain-of-Thought (CoT) code generator and an LLM-based code debugger, enhancing the controllability and robustness in generating guidance functions. Extensive experiments conducted on the nuScenes dataset demonstrate that LD-Scene achieves state-of-the-art performance in generating realistic, diverse, and effective adversarial scenarios. Furthermore, our framework provides fine-grained control over adversarial behaviors, thereby facilitating more effective testing tailored to specific driving scenarios.

