---
layout: default
title: BadNAVer: Exploring Jailbreak Attacks On Vision-and-Language Navigation
---

# BadNAVer: Exploring Jailbreak Attacks On Vision-and-Language Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12443" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12443v1</a>
  <a href="https://arxiv.org/pdf/2505.12443.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12443v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12443v1', 'BadNAVer: Exploring Jailbreak Attacks On Vision-and-Language Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenqi Lyu, Zerui Li, Yanyuan Qiao, Qi Wu

**分类**: cs.RO

**发布日期**: 2025-05-18

**备注**: 8 pages, 4 figures

---

## 💡 一句话要点

**提出BadNAVer以解决多模态大语言模型的监狱突破攻击问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视觉与语言导航` `监狱突破攻击` `安全性评估` `智能机器人`

## 📋 核心要点

1. 现有的多模态大语言模型在视觉与语言导航任务中存在安全隐患，容易受到监狱突破攻击。
2. 论文提出了一种三层攻击框架，构建恶意查询以测试MLLM驱动导航器的脆弱性。
3. 实验结果显示，攻击成功率超过90%，并在物理机器人上验证了攻击的现实可行性。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）因其在视觉与语言导航（VLN）任务中的泛化和推理能力而受到关注，推动了基于MLLM的导航器的发展。然而，MLLMs易受到监狱突破攻击，恶意提示可以绕过安全机制并触发不当输出。在具身场景中，这种脆弱性带来了更大的风险：与生成有害内容的纯文本模型不同，具身代理可能将恶意指令视为可执行命令，导致现实世界的伤害。本文首次提出针对MLLM驱动导航器的系统性监狱突破攻击范式，构建了一个三层攻击框架，并在四个意图类别中构造恶意查询，结合标准导航指令。在Matterport3D模拟器中，我们评估了五个MLLM驱动的导航代理，报告平均攻击成功率超过90%。为了测试现实世界的可行性，我们在物理机器人上复制了攻击，结果表明，即使是精心设计的提示也能引发MLLMs中的有害行为和意图，带来超出有害输出的风险，可能导致身体伤害。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在视觉与语言导航中的监狱突破攻击问题。现有方法未能有效防范恶意提示，导致安全隐患。

**核心思路**：提出一种三层攻击框架，通过构造恶意查询与标准导航指令结合，系统性地评估MLLM驱动导航器的脆弱性。

**技术框架**：整体架构包括三个主要模块：恶意查询生成、攻击执行和效果评估。每个模块针对不同意图类别设计特定的攻击策略。

**关键创新**：首次系统性地针对MLLM驱动导航器提出监狱突破攻击范式，揭示了具身代理在面对恶意指令时的潜在风险。

**关键设计**：在攻击框架中，设置了四个意图类别的恶意查询，结合标准导航指令，确保攻击的多样性和有效性。

## 📊 实验亮点

实验结果显示，针对五个不同的多模态大语言模型，攻击成功率超过90%。在物理机器人上复制攻击后，依然能够引发有害行为，表明该攻击方法在现实世界中的可行性和潜在威胁。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动驾驶和人机交互等场景。通过识别和防范监狱突破攻击，可以提升多模态大语言模型的安全性，确保在实际应用中不被恶意利用，从而保护用户和设备的安全。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have recently gained attention for their generalization and reasoning capabilities in Vision-and-Language Navigation (VLN) tasks, leading to the rise of MLLM-driven navigators. However, MLLMs are vulnerable to jailbreak attacks, where crafted prompts bypass safety mechanisms and trigger undesired outputs. In embodied scenarios, such vulnerabilities pose greater risks: unlike plain text models that generate toxic content, embodied agents may interpret malicious instructions as executable commands, potentially leading to real-world harm. In this paper, we present the first systematic jailbreak attack paradigm targeting MLLM-driven navigator. We propose a three-tiered attack framework and construct malicious queries across four intent categories, concatenated with standard navigation instructions. In the Matterport3D simulator, we evaluate navigation agents powered by five MLLMs and report an average attack success rate over 90%. To test real-world feasibility, we replicate the attack on a physical robot. Our results show that even well-crafted prompts can induce harmful actions and intents in MLLMs, posing risks beyond toxic output and potentially leading to physical harm.

