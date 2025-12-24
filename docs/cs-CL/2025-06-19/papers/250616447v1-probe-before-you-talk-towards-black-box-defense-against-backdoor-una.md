---
layout: default
title: "Probe before You Talk: Towards Black-box Defense against Backdoor Unalignment for Large Language Models"
---

# Probe before You Talk: Towards Black-box Defense against Backdoor Unalignment for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16447" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16447v1</a>
  <a href="https://arxiv.org/pdf/2506.16447.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16447v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16447v1', 'Probe before You Talk: Towards Black-box Defense against Backdoor Unalignment for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Biao Yi, Tiansheng Huang, Sishuo Chen, Tong Li, Zheli Liu, Zhixuan Chu, Yiming Li

**分类**: cs.CR, cs.CL

**发布日期**: 2025-06-19

**备注**: Accepted at ICLR 2025

**期刊**: Proceedings of The Thirteenth International Conference on Learning Representations (ICLR 2025)

---

## 💡 一句话要点

**提出BEAT以解决大型语言模型的后门不对齐问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `后门攻击` `大型语言模型` `黑箱防御` `安全对齐` `探测连接效应` `模型安全` `恶意探测` `流行越狱攻击`

## 📋 核心要点

1. 后门不对齐攻击使得大型语言模型的安全性受到严重威胁，现有防御方法难以有效识别和应对这种攻击。
2. 本文提出BEAT，通过探测连接效应来识别输入是否被触发，从而实现对后门的防御，克服了黑箱访问的限制。
3. 实验结果显示，BEAT在多种后门攻击场景中表现出色，能够有效降低后门模型的拒绝率，验证了其有效性和高效性。

## 📝 摘要（中文）

后门不对齐攻击对大型语言模型（LLMs）的安全性构成了严重威胁，这种攻击通过隐藏触发器悄然破坏安全对齐，并且能够规避正常的安全审计。本文提出了一种名为BEAT的黑箱防御方法，旨在检测推理过程中的触发样本，从而关闭后门。BEAT的核心思想是利用探测连接效应，通过测量输入与探测样本连接前后的输出分布扭曲程度来识别输入是否被触发。实验结果表明，BEAT在多种后门攻击和大型语言模型上均表现出良好的防御效果，并且能够有效抵御流行的越狱攻击。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型中的后门不对齐攻击问题。现有方法在面对样本依赖性攻击目标时表现不佳，难以有效识别被触发的输入样本。

**核心思路**：BEAT的核心思路是利用探测连接效应，通过分析输入与探测样本连接前后的输出分布变化，来判断输入是否被触发。这种方法从拒绝信号的角度出发，避免了样本特定的成功攻击行为的复杂性。

**技术框架**：BEAT的整体架构包括输入样本的接收、探测样本的生成、输出分布的测量和触发样本的识别四个主要模块。通过多次采样来近似输出分布，从而实现黑箱防御。

**关键创新**：BEAT的主要创新在于探测连接效应的引入，这一效应使得连接后的触发样本显著降低了后门模型对恶意探测的拒绝率，提供了一种新的防御思路。

**关键设计**：在参数设置上，BEAT采用了多次采样策略来提高输出分布的近似精度，并设计了特定的损失函数来优化探测效果，确保在黑箱环境下的有效性。实验中使用了多种大型语言模型，包括闭源的GPT-3.5-turbo，验证了方法的通用性。

## 📊 实验亮点

在多种后门攻击和大型语言模型的实验中，BEAT展示了优异的防御性能，显著降低了后门模型的拒绝率，验证了其在黑箱环境下的有效性和高效性。具体实验结果表明，BEAT在处理闭源模型时也能保持良好的防御效果。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的安全防护，尤其是在提供语言模型服务的商业环境中。BEAT的防御机制能够有效保护用户数据和模型安全，防止恶意攻击对模型的影响，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Backdoor unalignment attacks against Large Language Models (LLMs) enable the stealthy compromise of safety alignment using a hidden trigger while evading normal safety auditing. These attacks pose significant threats to the applications of LLMs in the real-world Large Language Model as a Service (LLMaaS) setting, where the deployed model is a fully black-box system that can only interact through text. Furthermore, the sample-dependent nature of the attack target exacerbates the threat. Instead of outputting a fixed label, the backdoored LLM follows the semantics of any malicious command with the hidden trigger, significantly expanding the target space. In this paper, we introduce BEAT, a black-box defense that detects triggered samples during inference to deactivate the backdoor. It is motivated by an intriguing observation (dubbed the probe concatenate effect), where concatenated triggered samples significantly reduce the refusal rate of the backdoored LLM towards a malicious probe, while non-triggered samples have little effect. Specifically, BEAT identifies whether an input is triggered by measuring the degree of distortion in the output distribution of the probe before and after concatenation with the input. Our method addresses the challenges of sample-dependent targets from an opposite perspective. It captures the impact of the trigger on the refusal signal (which is sample-independent) instead of sample-specific successful attack behaviors. It overcomes black-box access limitations by using multiple sampling to approximate the output distribution. Extensive experiments are conducted on various backdoor attacks and LLMs (including the closed-source GPT-3.5-turbo), verifying the effectiveness and efficiency of our defense. Besides, we also preliminarily verify that BEAT can effectively defend against popular jailbreak attacks, as they can be regarded as 'natural backdoors'.

