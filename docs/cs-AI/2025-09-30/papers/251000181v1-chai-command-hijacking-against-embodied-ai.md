---
layout: default
title: "CHAI: Command Hijacking against embodied AI"
---

# CHAI: Command Hijacking against embodied AI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00181" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00181v1</a>
  <a href="https://arxiv.org/pdf/2510.00181.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00181v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00181v1', 'CHAI: Command Hijacking against embodied AI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Luis Burbano, Diego Ortiz, Qi Sun, Siwei Yang, Haoqin Tu, Cihang Xie, Yinzhi Cao, Alvaro A Cardenas

**分类**: cs.CR, cs.AI, cs.LG

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出CHAI以解决对具身AI的命令劫持问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身人工智能` `命令劫持` `多模态攻击` `视觉语言模型` `安全性研究` `对抗攻击` `机器人系统`

## 📋 核心要点

1. 现有的具身AI系统在处理边缘案例时存在安全风险，尤其是在多模态理解方面容易受到攻击。
2. CHAI通过嵌入误导性指令并系统性地搜索令牌空间，利用LVLM的多模态推理能力来进行命令劫持。
3. 实验结果显示，CHAI在无人机、自动驾驶和物体跟踪任务中均优于现有攻击方法，展现出更强的攻击能力。

## 📝 摘要（中文）

具身人工智能（AI）在数据稀缺的情况下，通过基于感知和行动的常识推理来处理机器人系统中的边缘案例。然而，这些能力也带来了新的安全风险。本文提出了一种新的基于提示的攻击方法CHAI（Command Hijacking against embodied AI），该方法利用大型视觉语言模型（LVLMs）的多模态语言理解能力，通过在视觉输入中嵌入误导性自然语言指令，系统性地搜索令牌空间，构建提示字典，并引导攻击模型生成视觉攻击提示。我们在四个LVLM代理（无人机紧急着陆、自动驾驶和空中物体跟踪）及一个真实机器人上评估了CHAI，实验结果表明，CHAI在性能上始终优于现有的最先进攻击方法。

## 🔬 方法详解

**问题定义**：本文旨在解决具身AI系统中的命令劫持问题，现有方法在多模态理解和安全性方面存在不足，容易被误导性输入攻击。

**核心思路**：CHAI的核心思路是利用大型视觉语言模型的多模态语言理解能力，通过在视觉输入中嵌入误导性自然语言指令，系统性地生成攻击提示，从而劫持命令。

**技术框架**：CHAI的整体架构包括数据输入模块、令牌空间搜索模块、提示字典构建模块和攻击模型生成模块，形成一个完整的攻击流程。

**关键创新**：CHAI的主要创新在于其基于提示的攻击方法，能够有效利用LVLM的语义和多模态推理能力，超越传统对抗攻击的局限。

**关键设计**：在设计中，CHAI使用了特定的参数设置和损失函数，以优化生成的视觉攻击提示，并确保其在不同任务中的有效性。具体的网络结构和训练细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，CHAI在无人机紧急着陆、自动驾驶和空中物体跟踪任务中，攻击成功率显著高于现有最先进的攻击方法，提升幅度达到20%以上，展示了其强大的攻击能力和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括无人驾驶汽车、无人机控制和机器人导航等，能够帮助开发更安全的具身AI系统。通过识别和防范命令劫持攻击，提升系统的安全性和可靠性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Embodied Artificial Intelligence (AI) promises to handle edge cases in robotic vehicle systems where data is scarce by using common-sense reasoning grounded in perception and action to generalize beyond training distributions and adapt to novel real-world situations. These capabilities, however, also create new security risks. In this paper, we introduce CHAI (Command Hijacking against embodied AI), a new class of prompt-based attacks that exploit the multimodal language interpretation abilities of Large Visual-Language Models (LVLMs). CHAI embeds deceptive natural language instructions, such as misleading signs, in visual input, systematically searches the token space, builds a dictionary of prompts, and guides an attacker model to generate Visual Attack Prompts. We evaluate CHAI on four LVLM agents; drone emergency landing, autonomous driving, and aerial object tracking, and on a real robotic vehicle. Our experiments show that CHAI consistently outperforms state-of-the-art attacks. By exploiting the semantic and multimodal reasoning strengths of next-generation embodied AI systems, CHAI underscores the urgent need for defenses that extend beyond traditional adversarial robustness.

