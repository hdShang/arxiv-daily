---
layout: default
title: "AgentStealth: Reinforcing Large Language Model for Anonymizing User-generated Text"
---

# AgentStealth: Reinforcing Large Language Model for Anonymizing User-generated Text

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22508" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22508v1</a>
  <a href="https://arxiv.org/pdf/2506.22508.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22508v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22508v1', 'AgentStealth: Reinforcing Large Language Model for Anonymizing User-generated Text')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenyang Shao, Tianxing Li, Chenhao Pu, Fengli Xu, Yong Li

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-26

**备注**: This work has been submitted to NeurIPS 2025. Under review

**🔗 代码/项目**: [GITHUB](https://github.com/tsinghua-fib-lab/AgentStealth)

---

## 💡 一句话要点

**提出AgentStealth以解决用户生成文本匿名化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本匿名化` `用户隐私` `小规模语言模型` `对抗性学习` `强化学习`

## 📋 核心要点

1. 现有的文本匿名化方法要么损害文本的实用性，要么依赖于云端模型，存在隐私风险。
2. 本文提出了AgentStealth框架，通过对抗性匿名化和自适应控制，结合上下文对比学习来增强匿名化效果。
3. 实验结果显示，AgentStealth在两个数据集上分别提高了匿名化效果12.3%和实用性6.8%，表现优于现有基线。

## 📝 摘要（中文）

在当今数字世界中，用户生成的内容常常包含可能无意中暴露敏感个人属性的细微线索。这种风险凸显了有效文本匿名化的重要性，以保护个人隐私。然而，现有方法要么依赖于损害实用性的刚性替换，要么依赖于成本高且存在隐私风险的云端大语言模型（LLMs）。为了解决这些问题，本文探索了使用本地部署的小规模语言模型（SLMs）进行匿名化的可能性。我们提出了AgentStealth，一个自我强化的LLM匿名化框架，结合了对抗性匿名化工作流程、上下文对比学习和自适应实用性控制。实验结果表明，我们的方法在匿名化效果和实用性上均优于基线，且设计轻量，支持在边缘设备上直接部署，避免了对云的依赖和通信带来的隐私风险。

## 🔬 方法详解

**问题定义**：本文旨在解决用户生成文本中的敏感信息匿名化问题。现有方法往往通过简单替换来实现匿名化，导致文本实用性降低，或依赖云端模型，增加隐私泄露风险。

**核心思路**：我们提出的AgentStealth框架通过自我强化学习和对抗性匿名化工作流程，结合上下文对比学习，旨在提高小规模语言模型的匿名化效果和实用性。

**技术框架**：AgentStealth的整体架构包括三个主要模块：对抗性匿名化工作流程、监督适应和在线强化学习。首先，通过对抗性学习生成高质量的匿名化数据；其次，利用这些数据对小规模语言模型进行监督适应；最后，应用在线强化学习，利用内部对抗反馈不断优化模型性能。

**关键创新**：本文的主要创新在于引入了对抗性匿名化和上下文对比学习的结合，形成了一个自我强化的学习框架。这一方法与传统的刚性替换方法有本质区别，能够在保持文本实用性的同时有效进行匿名化。

**关键设计**：在设计中，我们采用了自适应控制机制来平衡匿名化效果与文本实用性，并使用高质量的标注数据进行监督学习。损失函数的设计考虑了匿名化效果和文本可读性之间的权衡。

## 📊 实验亮点

实验结果表明，AgentStealth在两个数据集上的匿名化效果提高了12.3%，实用性提升了6.8%。这些结果显著优于现有的基线方法，展示了该框架在文本匿名化领域的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体、在线评论和任何需要保护用户隐私的文本生成场景。通过在边缘设备上直接部署AgentStealth，可以有效降低云端依赖带来的隐私风险，提升用户对匿名化技术的信任度。未来，该技术有望在更多需要隐私保护的应用中得到广泛应用。

## 📄 摘要（原文）

> In today's digital world, casual user-generated content often contains subtle cues that may inadvertently expose sensitive personal attributes. Such risks underscore the growing importance of effective text anonymization to safeguard individual privacy. However, existing methods either rely on rigid replacements that damage utility or cloud-based LLMs that are costly and pose privacy risks. To address these issues, we explore the use of locally deployed smaller-scale language models (SLMs) for anonymization. Yet training effective SLMs remains challenging due to limited high-quality supervision. To address the challenge, we propose AgentStealth, a self-reinforcing LLM anonymization framework.First, we introduce an adversarial anonymization workflow enhanced by In-context Contrastive Learning and Adaptive Utility-Aware Control. Second, we perform supervised adaptation of SLMs using high-quality data collected from the workflow, which includes both anonymization and attack signals. Finally, we apply online reinforcement learning where the model leverages its internal adversarial feedback to iteratively improve anonymization performance. Experiments on two datasets show that our method outperforms baselines in both anonymization effectiveness (+12.3%) and utility (+6.8%). Our lightweight design supports direct deployment on edge devices, avoiding cloud reliance and communication-based privacy risks. Our code is open-source at https://github.com/tsinghua-fib-lab/AgentStealth.

