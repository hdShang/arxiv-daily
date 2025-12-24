---
layout: default
title: "DiffuGuard: How Intrinsic Safety is Lost and Found in Diffusion Large Language Models"
---

# DiffuGuard: How Intrinsic Safety is Lost and Found in Diffusion Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24296" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24296v1</a>
  <a href="https://arxiv.org/pdf/2509.24296.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24296v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24296v1', 'DiffuGuard: How Intrinsic Safety is Lost and Found in Diffusion Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zherui Li, Zheng Nie, Zhenhong Zhou, Yufei Guo, Yue Liu, Yitong Zhang, Yu Cheng, Qingsong Wen, Kun Wang, Jiaheng Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-29

**🔗 代码/项目**: [GITHUB](https://github.com/niez233/DiffuGuard)

---

## 💡 一句话要点

**DiffuGuard：揭示并修复扩散大语言模型中固有的安全漏洞**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散语言模型` `安全性` `越狱攻击` `防御框架` `随机退火` `风险检测` `文本生成` `深度学习`

## 📋 核心要点

1. 扩散语言模型面临新型安全威胁，其迭代生成方式与自回归模型不同，易受步内和步间动态攻击。
2. DiffuGuard通过随机退火重掩码和块级审计修复，在解码过程中引入随机性和风险检测，提升模型安全性。
3. 实验表明，DiffuGuard能显著降低越狱攻击成功率，从47.9%降至14.7%，同时保持模型性能和效率。

## 📝 摘要（中文）

扩散大语言模型(dLLMs)的快速发展带来了前所未有的安全漏洞，这些漏洞与自回归LLMs有着本质区别，源于其迭代和并行的生成机制。本文深入分析了dLLM在步内和步间动态方面的漏洞，以应对越狱攻击。实验结果揭示了标准贪婪重掩码策略中固有的有害偏差，并识别出一个关键现象，即去噪路径依赖性，其中早期token的安全性决定性地影响最终输出。这些发现表明，虽然当前的解码策略构成了一个重大漏洞，但dLLM具有巨大的内在安全潜力。为了释放这种潜力，我们提出了DiffuGuard，这是一个无需训练的防御框架，通过双阶段方法解决漏洞：随机退火重掩码动态引入受控随机性以减轻贪婪选择偏差，而块级审计和修复利用内部模型表示进行自主风险检测和引导校正。在四个dLLM上的综合实验表明，DiffuGuard具有卓越的有效性，针对六种不同的越狱方法，攻击成功率从47.9%降低到14.7%，同时保持了模型的效用和效率。

## 🔬 方法详解

**问题定义**：论文旨在解决扩散大语言模型（dLLMs）中存在的安全漏洞问题，特别是针对越狱攻击的脆弱性。现有的dLLMs由于其独特的迭代和并行生成机制，与自回归模型相比，面临着不同的安全挑战。标准的贪婪重掩码策略存在有害偏差，并且模型存在“去噪路径依赖性”，即早期token的安全性会显著影响最终输出的安全性。这些问题使得dLLMs容易受到恶意攻击，产生有害内容。

**核心思路**：DiffuGuard的核心思路是通过在解码过程中引入随机性和风险检测机制，来增强dLLMs的安全性。具体来说，它通过随机退火重掩码来减轻贪婪选择偏差，并通过块级审计和修复来检测和纠正潜在的风险内容。这种双阶段的方法旨在利用dLLMs内在的安全潜力，同时避免对模型进行重新训练。

**技术框架**：DiffuGuard是一个双阶段的防御框架，包含以下两个主要模块：
1. **随机退火重掩码（Stochastic Annealing Remasking）**：该模块通过动态引入受控的随机性来缓解贪婪选择偏差。它在重掩码过程中，并非总是选择概率最高的token，而是以一定的概率选择其他token，从而探索更多的生成路径。
2. **块级审计和修复（Block-level Audit and Repair）**：该模块利用模型的内部表示来检测和纠正潜在的风险内容。它将生成的文本分成块，并对每个块进行风险评估。如果检测到风险，则使用模型的内部信息来引导生成更安全的内容。

**关键创新**：DiffuGuard的关键创新在于其无需训练的防御机制，以及其双阶段的设计。与需要重新训练模型的防御方法不同，DiffuGuard可以直接应用于现有的dLLMs，而无需额外的训练成本。此外，其双阶段的设计能够有效地解决dLLMs中存在的两种主要漏洞：贪婪选择偏差和去噪路径依赖性。

**关键设计**：
* **随机退火重掩码**：引入退火参数来控制随机性的强度。退火参数随着解码的进行而逐渐降低，从而在早期阶段允许更多的探索，而在后期阶段则更加注重生成质量。
* **块级审计和修复**：使用预训练的风险检测模型来评估文本块的风险。如果检测到风险，则使用模型的梯度信息来引导生成更安全的内容。具体来说，它会计算风险检测模型对每个token的梯度，并使用这些梯度来调整token的概率分布，从而降低生成风险内容的可能性。

## 📊 实验亮点

DiffuGuard在四个不同的dLLMs上进行了评估，实验结果表明，该框架能够显著降低越狱攻击的成功率。具体来说，针对六种不同的越狱方法，DiffuGuard将攻击成功率从47.9%降低到14.7%。同时，DiffuGuard还能够保持模型的效用和效率，不会对模型的生成质量和速度产生显著影响。这些结果表明，DiffuGuard是一种有效的dLLMs防御方法。

## 🎯 应用场景

DiffuGuard具有广泛的应用前景，可以用于保护各种基于扩散模型的文本生成应用，例如聊天机器人、内容创作工具和代码生成器。通过提高dLLMs的安全性，DiffuGuard可以减少恶意攻击和有害内容的产生，从而促进这些技术的安全和可靠应用。此外，该研究还可以为未来dLLMs的安全设计提供指导。

## 📄 摘要（原文）

> The rapid advancement of Diffusion Large Language Models (dLLMs) introduces unprecedented vulnerabilities that are fundamentally distinct from Autoregressive LLMs, stemming from their iterative and parallel generation mechanisms. In this paper, we conduct an in-depth analysis of dLLM vulnerabilities to jailbreak attacks across two distinct dimensions: intra-step and inter-step dynamics. Experimental results reveal a harmful bias inherent in the standard greedy remasking strategy and identify a critical phenomenon we term Denoising-path Dependence, where the safety of early-stage tokens decisively influences the final output. These findings also indicate that while current decoding strategies constitute a significant vulnerability, dLLMs possess a substantial intrinsic safety potential. To unlock this potential, we propose DiffuGuard, a training-free defense framework that addresses vulnerabilities through a dual-stage approach: Stochastic Annealing Remasking dynamically introduces controlled randomness to mitigate greedy selection bias, while Block-level Audit and Repair exploits internal model representations for autonomous risk detection and guided correction. Comprehensive experiments on four dLLMs demonstrate DiffuGuard's exceptional effectiveness, reducing Attack Success Rate against six diverse jailbreak methods from 47.9% to 14.7% while preserving model utility and efficiency. Our code is available at: https://github.com/niez233/DiffuGuard.

