---
layout: default
title: "From Injection to Defense: Constructing Edit-Based Fingerprints for Large Language Models"
---

# From Injection to Defense: Constructing Edit-Based Fingerprints for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03122" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03122v2</a>
  <a href="https://arxiv.org/pdf/2509.03122.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03122v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03122v2', 'From Injection to Defense: Constructing Edit-Based Fingerprints for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yue Li, Xin Yi, Dongsheng Shi, Yongyi Cui, Gerard de Melo, Linlin Wang

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-03 (更新: 2025-10-08)

**备注**: preprint

---

## 💡 一句话要点

**提出RFEdit框架，通过知识编辑为大语言模型构建基于编辑的指纹，并提出FSFT进行防御。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `指纹识别` `知识产权保护` `知识编辑` `模型安全`

## 📋 核心要点

1. 现有指纹方法在鲁棒性和隐蔽性之间存在权衡，乱码指纹易被检测，自然语言指纹易被误触发。
2. RFEdit通过知识编辑，修改模型权重稀疏子集来嵌入多语言自然语言指纹，实现高效鲁棒的指纹注入。
3. FSFT限制参数更新到指纹子空间，减轻微调期间指纹退化，同时增强下游任务性能，实验表明其有效性。

## 📝 摘要（中文）

指纹识别对于维护可追溯性并保护开发者的知识产权至关重要，因为部署在Web应用程序中的LLM容易受到未经授权的重新分发和通过微调或黑盒部署的滥用。然而，目前基于后门的指纹识别方法面临着一个根本性的权衡：嵌入为乱码文本的指纹很容易被检测和过滤，而那些被设计为连贯自然语言的指纹容易被意外触发。为了克服这些限制，我们提出了RFEdit，这是一个知识编辑框架，通过修改模型权重的稀疏子集来嵌入基于规则的多语言自然语言指纹（MNLF）。这种方法能够实现高效且鲁棒的指纹注入，同时最大限度地减少对LLM中不相关知识的影响。我们的RFEdit框架通过指纹子空间感知微调（FSFT）进一步得到保护，该方法通过限制参数更新到指纹子空间来减轻合法微调期间的指纹退化。这种方法在增强LLM的下游任务性能的同时，保持了指纹的完整性。这些进展建立了一个从指纹注入到防御的综合流程，实现了高检测有效性、对抗性操纵的鲁棒性、对模型效用的无害性以及在微调下的持久性。大量的实验表明，RFEdit在量化和剪枝下保持了鲁棒性。此外，当与FSFT结合用于数学和alpaca下游任务时，指纹有效性通常提高了10％以上。

## 🔬 方法详解

**问题定义**：论文旨在解决大语言模型（LLM）的知识产权保护问题，防止未经授权的重新分发和滥用。现有基于后门的指纹识别方法存在鲁棒性和隐蔽性的trade-off：乱码指纹容易被检测和过滤，而自然语言指纹容易被意外触发，影响模型性能。

**核心思路**：论文的核心思路是通过知识编辑的方式，在LLM的权重中嵌入指纹，同时保证指纹的鲁棒性和隐蔽性。具体来说，通过修改模型权重的稀疏子集来嵌入多语言自然语言指纹（MNLF），并设计指纹子空间感知微调（FSFT）来抵抗微调带来的指纹退化。

**技术框架**：该框架包含两个主要阶段：指纹注入和指纹防御。指纹注入阶段使用RFEdit框架，通过知识编辑将MNLF嵌入到LLM的权重中。指纹防御阶段使用FSFT方法，在微调过程中限制参数更新到指纹子空间，以保持指纹的完整性。整体流程是从指纹注入到防御的综合流程。

**关键创新**：论文的关键创新在于提出了基于知识编辑的指纹注入方法RFEdit和指纹子空间感知微调FSFT。RFEdit通过修改模型权重的稀疏子集来嵌入指纹，避免了对模型整体性能的显著影响。FSFT通过限制参数更新到指纹子空间，有效地抵抗了微调带来的指纹退化，同时提升了下游任务的性能。与现有方法相比，该方法在鲁棒性、隐蔽性和模型效用之间取得了更好的平衡。

**关键设计**：RFEdit框架的关键设计包括：1) 基于规则的多语言自然语言指纹（MNLF）的设计，保证了指纹的可读性和可解释性；2) 稀疏权重修改策略，最小化对模型性能的影响；3) 指纹子空间感知微调（FSFT），通过限制参数更新到指纹子空间来保持指纹的完整性。FSFT的具体实现可能涉及到定义指纹子空间的损失函数，以及在微调过程中对参数更新进行约束。

## 📊 实验亮点

实验结果表明，RFEdit在量化和剪枝下保持了鲁棒性。与FSFT结合后，在数学和Alpaca下游任务中，指纹有效性通常提高了10%以上。这些结果表明，该方法在保证指纹鲁棒性的同时，能够有效提升模型的下游任务性能。

## 🎯 应用场景

该研究成果可应用于大语言模型的知识产权保护，防止模型被恶意复制、篡改或用于非法用途。例如，开发者可以将指纹嵌入到其发布的LLM中，以便在发现未经授权的使用时进行追溯和维权。此外，该技术还可以用于评估模型的安全性，检测模型是否被植入恶意后门。

## 📄 摘要（原文）

> Fingerprinting is critical for maintaining traceability and protecting the intellectual property (IP) of developers, as LLMs deployed in web applications are susceptible to unauthorized redistribution and misuse via fine-tuning or black-box deployment. However, current backdoor-based fingerprinting methods face a fundamental trade-off: fingerprints embedded as garbled text are easily detected and filtered, whereas those crafted as coherent natural language are prone to being triggered unintentionally. To overcome these limitations, we propose RFEdit, a knowledge-editing framework that embeds a rule-based multilingual natural language fingerprint (MNLF) by modifying a sparse subset of model weights. This approach enables efficient and robust fingerprint injection with minimal impact on unrelated knowledge in LLMs. Our RFEdit framework is further safeguarded by Fingerprint Subspace-aware Fine-Tuning (FSFT), which mitigates fingerprint degradation during legitimate fine-tuning by restricting parameter updates to the fingerprint subspace. This approach preserves fingerprint integrity while enhancing downstream task performance of LLMs. These advances establish a comprehensive pipeline from fingerprint injection to defense, achieving high detection effectiveness, robustness against adversarial manipulations, harmlessness to model utility, and persistence under fine-tuning. Extensive experiments demonstrate that RFEdit maintains robustness under quantization and pruning. Additionally, fingerprint effectiveness is generally improved by more than 10\% when combined with FSFT for math and alpaca downstream tasks.

