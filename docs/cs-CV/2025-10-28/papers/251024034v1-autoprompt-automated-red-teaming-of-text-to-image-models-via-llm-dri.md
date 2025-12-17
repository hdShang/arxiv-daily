---
layout: default
title: AutoPrompt: Automated Red-Teaming of Text-to-Image Models via LLM-Driven Adversarial Prompts
---

# AutoPrompt: Automated Red-Teaming of Text-to-Image Models via LLM-Driven Adversarial Prompts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.24034" class="toolbar-btn" target="_blank">📄 arXiv: 2510.24034v1</a>
  <a href="https://arxiv.org/pdf/2510.24034.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.24034v1" onclick="toggleFavorite(this, '2510.24034v1', 'AutoPrompt: Automated Red-Teaming of Text-to-Image Models via LLM-Driven Adversarial Prompts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yufan Liu, Wanqian Zhang, Huashan Chen, Lin Wang, Xiaojun Jia, Zheng Lin, Weiping Wang

**分类**: cs.CV

**发布日期**: 2025-10-28

**备注**: Accepted by ICCV 2025

---

## 💡 一句话要点

**提出AutoPrompt，利用LLM自动生成对抗性提示，实现对文本到图像模型的黑盒红队测试。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到图像模型` `对抗性攻击` `红队测试` `大型语言模型` `黑盒攻击`

## 📋 核心要点

1. 文本到图像模型易受对抗性提示攻击，现有红队测试方法依赖白盒访问和低效的逐提示优化，且易生成无意义提示。
2. AutoPrompt利用LLM生成人类可读的对抗性后缀，通过交替优化和微调，提升对抗性提示的生成质量和效率。
3. 实验表明，AutoPrompt生成的提示具有优秀的红队测试性能和零样本迁移能力，能有效攻击商业API。

## 📝 摘要（中文）

本文提出AutoPrompt (APT)，一个黑盒框架，利用大型语言模型(LLM)为良性提示自动生成人类可读的对抗性后缀，从而实现对文本到图像(T2I)模型的红队测试。该框架首先引入对抗性后缀优化和LLM微调之间的交替优化-微调流程，并利用优化后的后缀对LLM进行微调。此外，在优化阶段集成了双重规避策略，以绕过基于困惑度的过滤器和黑名单词过滤器：(1) 通过辅助LLM困惑度评分约束LLM生成人类可读的提示，这与之前的token级别乱码形成鲜明对比；(2) 引入禁用token惩罚，以抑制黑名单中禁用token的显式生成。大量实验表明，我们的人类可读、抗过滤的对抗性提示具有出色的红队测试性能，以及卓越的零样本迁移能力，能够即时适应未见过的提示，并暴露商业API（例如Leonardo.Ai）中的关键漏洞。

## 🔬 方法详解

**问题定义**：文本到图像(T2I)模型虽然发展迅速，但其安全机制容易受到对抗性提示的攻击，这些提示会恶意生成不安全的图像。现有的红队测试方法通常需要白盒访问T2I模型，并且依赖于低效的逐提示优化，而且不可避免地会生成语义上无意义的提示，这些提示很容易被过滤器阻止。因此，需要一种黑盒方法，能够自动生成人类可读且能绕过过滤器的对抗性提示，以有效评估T2I模型的安全性。

**核心思路**：AutoPrompt的核心思路是利用大型语言模型(LLM)生成对抗性后缀，并将其添加到良性提示中，从而欺骗T2I模型生成不安全的图像。通过优化LLM生成的后缀，使其既能有效攻击T2I模型，又能保持人类可读性并绕过各种过滤器。这种方法的核心在于利用LLM的生成能力和优化算法的搜索能力，自动发现有效的对抗性提示。

**技术框架**：AutoPrompt框架包含以下主要模块：1) **对抗性后缀优化**：使用优化算法（如梯度下降）搜索能够最大化攻击成功率的对抗性后缀。2) **LLM微调**：利用优化后的对抗性后缀对LLM进行微调，提高LLM生成对抗性提示的能力。3) **双重规避策略**：包括基于困惑度的过滤器规避和黑名单词过滤器规避。4) **交替优化-微调流程**：在对抗性后缀优化和LLM微调之间进行交替，不断提高对抗性提示的质量和LLM的生成能力。

**关键创新**：AutoPrompt的关键创新在于：1) **黑盒攻击**：无需访问T2I模型的内部参数，即可进行红队测试。2) **人类可读的对抗性提示**：生成的提示具有良好的可读性，更难被过滤器识别和阻止。3) **双重规避策略**：能够有效绕过基于困惑度的过滤器和黑名单词过滤器。4) **交替优化-微调流程**：能够不断提高对抗性提示的质量和LLM的生成能力。与现有方法的本质区别在于，AutoPrompt利用LLM的生成能力和优化算法的搜索能力，自动发现有效的对抗性提示，而无需人工设计或修改提示。

**关键设计**：AutoPrompt的关键设计包括：1) **困惑度约束**：通过计算LLM生成提示的困惑度，约束其生成人类可读的提示。2) **禁用token惩罚**：对LLM生成黑名单中的token进行惩罚，防止其生成包含敏感词汇的提示。3) **交替优化-微调的超参数设置**：例如，优化算法的学习率、微调的epoch数等。4) **对抗性损失函数的设计**：用于衡量攻击的成功率，例如，可以根据生成的图像是否包含不安全内容来设计损失函数。

## 📊 实验亮点

实验结果表明，AutoPrompt生成的对抗性提示具有出色的红队测试性能，能够有效攻击各种文本到图像模型，包括商业API（例如Leonardo.Ai）。AutoPrompt还具有卓越的零样本迁移能力，能够即时适应未见过的提示，并暴露模型中的关键漏洞。与现有方法相比，AutoPrompt生成的提示更具可读性，且更难被过滤器阻止。

## 🎯 应用场景

AutoPrompt可用于评估和提高文本到图像模型的安全性，帮助开发者发现和修复潜在的安全漏洞。该技术可应用于各种场景，例如，评估商业API的安全性、开发更安全的文本到图像模型、以及防止恶意用户利用对抗性提示生成不安全内容。未来的研究可以探索更有效的对抗性提示生成方法，以及更鲁棒的防御机制。

## 📄 摘要（原文）

> Despite rapid advancements in text-to-image (T2I) models, their safety mechanisms are vulnerable to adversarial prompts, which maliciously generate unsafe images. Current red-teaming methods for proactively assessing such vulnerabilities usually require white-box access to T2I models, and rely on inefficient per-prompt optimization, as well as inevitably generate semantically meaningless prompts easily blocked by filters. In this paper, we propose APT (AutoPrompT), a black-box framework that leverages large language models (LLMs) to automatically generate human-readable adversarial suffixes for benign prompts. We first introduce an alternating optimization-finetuning pipeline between adversarial suffix optimization and fine-tuning the LLM utilizing the optimized suffix. Furthermore, we integrates a dual-evasion strategy in optimization phase, enabling the bypass of both perplexity-based filter and blacklist word filter: (1) we constrain the LLM generating human-readable prompts through an auxiliary LLM perplexity scoring, which starkly contrasts with prior token-level gibberish, and (2) we also introduce banned-token penalties to suppress the explicit generation of banned-tokens in blacklist. Extensive experiments demonstrate the excellent red-teaming performance of our human-readable, filter-resistant adversarial prompts, as well as superior zero-shot transferability which enables instant adaptation to unseen prompts and exposes critical vulnerabilities even in commercial APIs (e.g., Leonardo.Ai.).

