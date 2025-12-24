---
layout: default
title: "When Good Sounds Go Adversarial: Jailbreaking Audio-Language Models with Benign Inputs"
---

# When Good Sounds Go Adversarial: Jailbreaking Audio-Language Models with Benign Inputs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03365" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03365v2</a>
  <a href="https://arxiv.org/pdf/2508.03365.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03365v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03365v2', 'When Good Sounds Go Adversarial: Jailbreaking Audio-Language Models with Benign Inputs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bodam Kim, Hiskias Dingeto, Taeyoun Kwon, Dasol Choi, DongGeon Lee, Haon Park, JaeHoon Lee, Jongho Shin

**分类**: cs.SD, cs.AI, cs.CR, eess.AS

**发布日期**: 2025-08-05 (更新: 2025-08-20)

---

## 💡 一句话要点

**提出WhisperInject框架以破解音频语言模型的安全性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对抗攻击` `音频语言模型` `安全性` `强化学习` `微小扰动` `人机交互` `模型操控`

## 📋 核心要点

1. 现有音频语言模型在安全性方面存在漏洞，容易受到对抗攻击，导致生成有害内容。
2. WhisperInject框架通过两阶段的对抗攻击，利用微小的音频扰动操控模型生成有害响应。
3. 实验验证显示，WhisperInject在多个音频语言模型上的成功率超过86%，显著提升了对抗攻击的有效性。

## 📝 摘要（中文）

随着大型语言模型日益融入日常生活，音频作为人机交互的关键接口也带来了新的安全隐患。本研究提出了WhisperInject，一个两阶段的对抗音频攻击框架，能够操控最先进的音频语言模型生成有害内容。该方法利用对人类听众无感知的音频输入扰动，第一阶段采用了一种新颖的基于奖励的优化方法，强化学习与投影梯度下降（RL-PGD），引导目标模型绕过自身的安全协议，生成有害的原生响应。第二阶段为有效载荷注入，通过投影梯度下降（PGD）优化嵌入在无害音频载体中的微小扰动。实验结果表明，在多个模型上成功率超过86%。

## 🔬 方法详解

**问题定义**：本研究旨在解决音频语言模型在安全性方面的脆弱性，现有方法未能有效防范对抗攻击，导致模型生成有害内容的风险增加。

**核心思路**：WhisperInject框架通过两阶段的对抗攻击策略，首先生成有害的原生响应，然后通过微小扰动嵌入到无害音频中，从而实现对模型的操控。

**技术框架**：该框架分为两个主要阶段：第一阶段使用强化学习与投影梯度下降（RL-PGD）优化模型响应，第二阶段通过投影梯度下降（PGD）将扰动注入到无害音频载体中。

**关键创新**：本研究的创新在于提出了一种新的攻击框架，结合了奖励机制和对抗扰动，能够有效绕过模型的安全协议，与传统的对抗攻击方法相比，具有更高的隐蔽性和有效性。

**关键设计**：在第一阶段，采用了基于奖励的优化策略，确保生成的响应能够有效绕过安全机制；在第二阶段，设计了精细的扰动注入策略，确保对人类听众无感知，同时又能影响模型输出。

## 📊 实验亮点

实验结果显示，WhisperInject在Qwen2.5-Omni-3B、Qwen2.5-Omni-7B和Phi-4-Multimodal等多个模型上的成功率超过86%。这一结果显著高于现有对抗攻击方法，表明该框架在实际应用中的有效性和潜力。

## 🎯 应用场景

WhisperInject框架的潜在应用场景包括音频助手、智能音箱等人机交互系统。通过识别和修复音频模型的安全漏洞，可以提升这些系统的安全性和可靠性，防止恶意攻击对用户造成的影响。未来，该研究可能推动音频处理和安全防护技术的发展。

## 📄 摘要（原文）

> As large language models become increasingly integrated into daily life, audio has emerged as a key interface for human-AI interaction. However, this convenience also introduces new vulnerabilities, making audio a potential attack surface for adversaries. Our research introduces WhisperInject, a two-stage adversarial audio attack framework that can manipulate state-of-the-art audio language models to generate harmful content. Our method uses imperceptible perturbations in audio inputs that remain benign to human listeners. The first stage uses a novel reward-based optimization method, Reinforcement Learning with Projected Gradient Descent (RL-PGD), to guide the target model to circumvent its own safety protocols and generate harmful native responses. This native harmful response then serves as the target for Stage 2, Payload Injection, where we use Projected Gradient Descent (PGD) to optimize subtle perturbations that are embedded into benign audio carriers, such as weather queries or greeting messages. Validated under the rigorous StrongREJECT, LlamaGuard, as well as Human Evaluation safety evaluation framework, our experiments demonstrate a success rate exceeding 86% across Qwen2.5-Omni-3B, Qwen2.5-Omni-7B, and Phi-4-Multimodal. Our work demonstrates a new class of practical, audio-native threats, moving beyond theoretical exploits to reveal a feasible and covert method for manipulating AI behavior.

