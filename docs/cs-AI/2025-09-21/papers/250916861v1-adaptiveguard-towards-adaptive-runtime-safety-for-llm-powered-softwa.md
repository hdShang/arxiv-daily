---
layout: default
title: "AdaptiveGuard: Towards Adaptive Runtime Safety for LLM-Powered Software"
---

# AdaptiveGuard: Towards Adaptive Runtime Safety for LLM-Powered Software

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16861" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16861v1</a>
  <a href="https://arxiv.org/pdf/2509.16861.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16861v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16861v1', 'AdaptiveGuard: Towards Adaptive Runtime Safety for LLM-Powered Software')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rui Yang, Michael Fu, Chakkrit Tantithamthavorn, Chetan Arora, Gunel Gulmammadova, Joey Chua

**分类**: cs.CR, cs.AI, cs.SE

**发布日期**: 2025-09-21

**备注**: Accepted to the ASE 2025 International Conference on Automated Software Engineering, Industry Showcase Track

**🔗 代码/项目**: [GITHUB](https://github.com/awsm-research/AdaptiveGuard)

---

## 💡 一句话要点

**AdaptiveGuard：面向LLM软件的自适应运行时安全防护**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型安全` `越狱攻击防御` `自适应Guardrail` `分布外检测` `持续学习`

## 📋 核心要点

1. 现有LLM guardrails在面对新型越狱攻击时性能显著下降，无法有效应对不断演进的威胁。
2. AdaptiveGuard通过将新型攻击识别为分布外数据，并利用持续学习框架动态适应和防御这些攻击。
3. 实验表明，AdaptiveGuard在OOD检测、适应速度和性能保持方面均优于现有方法，展现了其有效性。

## 📝 摘要（中文）

Guardrails对于保障大语言模型（LLM）驱动软件的安全部署至关重要。与输入输出空间受限的传统规则系统不同，LLM支持开放式、智能交互，但也为通过用户输入发起的越狱攻击打开了大门。Guardrails作为保护层，过滤不安全的提示。然而，现有研究表明，即使是GPT-4o等先进模型，越狱攻击的成功率仍然超过70%。尽管LlamaGuard等guardrails的准确率高达95%，但我们的初步分析表明，面对未知的攻击时，其性能可能会急剧下降至12%。这突显了一个日益严峻的软件工程挑战：如何构建一个能够动态适应新威胁的部署后guardrail？为了解决这个问题，我们提出了AdaptiveGuard，一种自适应guardrail，它将新的越狱攻击检测为分布外（OOD）输入，并通过持续学习框架学习防御它们。通过实证评估，AdaptiveGuard实现了96%的OOD检测准确率，仅需两个更新步骤即可适应新的攻击，并在适应后保持超过85%的F1分数，优于其他基线。这些结果表明，AdaptiveGuard是一种能够响应部署后出现的新越狱策略的guardrail。我们发布了AdaptiveGuard和研究数据集，以支持进一步的研究。

## 🔬 方法详解

**问题定义**：论文旨在解决LLM驱动软件面临的越狱攻击问题。现有的guardrails方法，如LlamaGuard，在面对未知的、新型的越狱攻击时，性能会显著下降，无法提供可靠的运行时安全保障。这些方法通常基于预定义的规则或已知的攻击模式进行防御，缺乏对未知攻击的适应能力。

**核心思路**：AdaptiveGuard的核心思路是将新型越狱攻击视为分布外（Out-of-Distribution, OOD）的输入，并利用持续学习（Continual Learning）框架来动态地学习和适应这些新的攻击模式。通过OOD检测，AdaptiveGuard能够识别出未知的攻击，然后通过持续学习，不断更新其防御策略，从而提高对新型攻击的防御能力。

**技术框架**：AdaptiveGuard的整体框架包含以下几个主要模块：1) **OOD检测模块**：用于检测输入是否为分布外数据，即是否为新型的越狱攻击。2) **持续学习模块**：当检测到OOD输入时，该模块会利用新的攻击数据来更新guardrail的模型参数，从而提高对新型攻击的防御能力。3) **Guardrail模块**：基于更新后的模型参数，对输入进行过滤，防止恶意提示到达LLM。整个流程是，输入首先经过OOD检测，如果被识别为OOD，则触发持续学习模块进行模型更新，然后Guardrail模块使用更新后的模型进行过滤。

**关键创新**：AdaptiveGuard的关键创新在于其自适应性，能够动态地学习和适应新型的越狱攻击。与传统的静态guardrails相比，AdaptiveGuard能够不断进化，从而更好地应对不断变化的威胁。此外，将OOD检测与持续学习相结合，使得AdaptiveGuard能够有效地识别和防御未知的攻击。

**关键设计**：AdaptiveGuard的具体实现细节包括：OOD检测模块可以使用各种OOD检测算法，例如基于距离的方法或基于密度的方法。持续学习模块可以使用各种持续学习算法，例如iCaRL或EWC。Guardrail模块可以使用各种文本分类模型，例如BERT或RoBERTa。论文中可能使用了特定的参数设置和损失函数来优化模型的性能，但具体细节未知。

## 📊 实验亮点

AdaptiveGuard在实验中表现出色，实现了96%的OOD检测准确率，能够有效识别新型越狱攻击。仅需两个更新步骤，AdaptiveGuard即可适应新的攻击模式，展现了其快速适应能力。在适应新攻击后，AdaptiveGuard仍能保持超过85%的F1分数，表明其在提高防御能力的同时，能够有效避免遗忘已学习的知识。AdaptiveGuard的性能优于其他基线方法，证明了其在运行时安全防护方面的优势。

## 🎯 应用场景

AdaptiveGuard可应用于各种LLM驱动的软件系统中，例如聊天机器人、智能助手、代码生成工具等。通过提供自适应的运行时安全防护，AdaptiveGuard可以有效防止恶意用户利用越狱攻击来操纵LLM，从而保障系统的安全性和可靠性。该研究对于推动LLM在安全敏感领域的应用具有重要意义。

## 📄 摘要（原文）

> Guardrails are critical for the safe deployment of Large Language Models (LLMs)-powered software. Unlike traditional rule-based systems with limited, predefined input-output spaces that inherently constrain unsafe behavior, LLMs enable open-ended, intelligent interactions--opening the door to jailbreak attacks through user inputs. Guardrails serve as a protective layer, filtering unsafe prompts before they reach the LLM. However, prior research shows that jailbreak attacks can still succeed over 70% of the time, even against advanced models like GPT-4o. While guardrails such as LlamaGuard report up to 95% accuracy, our preliminary analysis shows their performance can drop sharply--to as low as 12%--when confronted with unseen attacks. This highlights a growing software engineering challenge: how to build a post-deployment guardrail that adapts dynamically to emerging threats? To address this, we propose AdaptiveGuard, an adaptive guardrail that detects novel jailbreak attacks as out-of-distribution (OOD) inputs and learns to defend against them through a continual learning framework. Through empirical evaluation, AdaptiveGuard achieves 96% OOD detection accuracy, adapts to new attacks in just two update steps, and retains over 85% F1-score on in-distribution data post-adaptation, outperforming other baselines. These results demonstrate that AdaptiveGuard is a guardrail capable of evolving in response to emerging jailbreak strategies post deployment. We release our AdaptiveGuard and studied datasets at https://github.com/awsm-research/AdaptiveGuard to support further research.

