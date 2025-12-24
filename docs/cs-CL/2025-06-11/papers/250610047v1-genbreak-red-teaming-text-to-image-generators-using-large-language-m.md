---
layout: default
title: "GenBreak: Red Teaming Text-to-Image Generators Using Large Language Models"
---

# GenBreak: Red Teaming Text-to-Image Generators Using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10047" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10047v1</a>
  <a href="https://arxiv.org/pdf/2506.10047.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10047v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10047v1', 'GenBreak: Red Teaming Text-to-Image Generators Using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zilong Wang, Xiang Zheng, Xiaosen Wang, Bo Wang, Xingjun Ma, Yu-Gang Jiang

**分类**: cs.CR, cs.CL

**发布日期**: 2025-06-11

**备注**: 27 pages, 7 figures

---

## 💡 一句话要点

**提出GenBreak框架以评估文本生成图像模型的安全性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本生成图像` `安全评估` `对抗攻击` `大型语言模型` `红队测试` `强化学习` `内容创作`

## 📋 核心要点

1. 现有的对抗攻击研究在生成有害内容方面存在局限，未能有效发现高风险提示，导致安全评估工具的缺乏。
2. 本文提出GenBreak框架，通过微调大型语言模型，结合监督学习和强化学习，系统性探索T2I模型的安全漏洞。
3. 实验结果表明，GenBreak生成的对抗提示在黑箱攻击中表现出色，揭示了商业T2I生成器的安全弱点。

## 📝 摘要（中文）

文本生成图像（T2I）模型如Stable Diffusion迅速发展并广泛应用于内容创作。然而，这些模型可能被滥用生成有害内容，带来安全风险。现有的红队测试和对抗攻击研究存在局限，未能有效发现高风险提示。为此，本文提出GenBreak框架，通过微调大型语言模型（LLM）系统性探索T2I生成器的潜在漏洞。该方法结合监督微调和强化学习，指导LLM生成具有高毒性和语义一致性的对抗提示，展示了在商业T2I生成器上的有效性，揭示了实际的安全隐患。

## 🔬 方法详解

**问题定义**：本文旨在解决文本生成图像（T2I）模型在安全性评估中的不足，现有方法无法有效生成高风险提示，导致安全漏洞难以发现。

**核心思路**：通过微调大型语言模型（LLM），结合监督学习和强化学习，系统性探索T2I生成器的潜在漏洞，从而生成更具毒性的对抗提示。

**技术框架**：整体架构包括数据集的监督微调阶段和与替代T2I模型的交互强化学习阶段，整合多种奖励信号以指导模型生成对抗提示。

**关键创新**：最重要的创新在于将多种奖励信号结合，提升了对抗提示的生成能力，既能规避安全过滤器，又能保持语义一致性和多样性。

**关键设计**：在参数设置上，采用了特定的损失函数和网络结构，以优化生成的对抗提示的毒性和有效性，同时确保与T2I模型的兼容性。

## 📊 实验亮点

实验结果显示，GenBreak生成的对抗提示在黑箱攻击中表现优异，相较于现有方法，成功率显著提升，揭示了商业T2I生成器的安全弱点，具有重要的实用价值。

## 🎯 应用场景

该研究的潜在应用领域包括内容创作平台的安全性评估、对抗性测试工具的开发以及AI生成内容的监管。通过提供有效的安全评估工具，能够帮助平台识别和防范潜在的有害内容生成，提升用户安全体验。

## 📄 摘要（原文）

> Text-to-image (T2I) models such as Stable Diffusion have advanced rapidly and are now widely used in content creation. However, these models can be misused to generate harmful content, including nudity or violence, posing significant safety risks. While most platforms employ content moderation systems, underlying vulnerabilities can still be exploited by determined adversaries. Recent research on red-teaming and adversarial attacks against T2I models has notable limitations: some studies successfully generate highly toxic images but use adversarial prompts that are easily detected and blocked by safety filters, while others focus on bypassing safety mechanisms but fail to produce genuinely harmful outputs, neglecting the discovery of truly high-risk prompts. Consequently, there remains a lack of reliable tools for evaluating the safety of defended T2I models. To address this gap, we propose GenBreak, a framework that fine-tunes a red-team large language model (LLM) to systematically explore underlying vulnerabilities in T2I generators. Our approach combines supervised fine-tuning on curated datasets with reinforcement learning via interaction with a surrogate T2I model. By integrating multiple reward signals, we guide the LLM to craft adversarial prompts that enhance both evasion capability and image toxicity, while maintaining semantic coherence and diversity. These prompts demonstrate strong effectiveness in black-box attacks against commercial T2I generators, revealing practical and concerning safety weaknesses.

