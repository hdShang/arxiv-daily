---
layout: default
title: "Differential Robustness in Transformer Language Models: Empirical Evaluation Under Adversarial Text Attacks"
---

# Differential Robustness in Transformer Language Models: Empirical Evaluation Under Adversarial Text Attacks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09706" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09706v1</a>
  <a href="https://arxiv.org/pdf/2509.09706.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09706v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09706v1', 'Differential Robustness in Transformer Language Models: Empirical Evaluation Under Adversarial Text Attacks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Taniya Gidatkar, Oluwaseun Ajao, Matthew Shardlow

**分类**: cs.CR, cs.AI, cs.CL

**发布日期**: 2025-09-05

**备注**: 8 pages, 4 tables, to appear in proceedings of Recent Advances in Natural Language Processing (RANLP 2025) and ACL Anthology

---

## 💡 一句话要点

**评估Transformer语言模型在对抗文本攻击下的鲁棒性差异**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `对抗攻击` `鲁棒性评估` `Transformer模型` `TextFooler` `BERTAttack` `模型安全性`

## 📋 核心要点

1. 现有大型语言模型在面对对抗性文本攻击时，鲁棒性表现参差不齐，缺乏系统性的评估和理解。
2. 通过对抗性攻击测试，分析不同Transformer模型在面对恶意文本扰动时的性能下降情况，揭示其内在脆弱性。
3. 实验结果表明，RoBERTa-Base和FlanT5具有较强的鲁棒性，而BERT-Base则相对脆弱，为后续防御策略提供了依据。

## 📝 摘要（中文）

本研究评估了大型语言模型（LLMs）在对抗性攻击下的鲁棒性，重点关注Flan-T5、BERT和RoBERTa-Base。通过TextFooler和BERTAttack系统设计的对抗测试，我们发现模型鲁棒性存在显著差异。RoBERTa-Base和FlanT5表现出卓越的鲁棒性，即使在受到复杂攻击时也能保持准确性，攻击成功率为0%。相比之下，BERT-Base表现出相当大的脆弱性，TextFooler成功地将其准确率从48%降低到仅3%，成功率高达93.75%。我们的研究表明，虽然某些LLM已经开发出有效的防御机制，但这些保护措施通常需要大量的计算资源。本研究通过识别当前保护方法中存在的优势和劣势，为理解LLM安全性做出了贡献，并为开发更高效和有效的防御策略提出了实用的建议。

## 🔬 方法详解

**问题定义**：论文旨在研究大型语言模型（LLMs）在面对对抗性文本攻击时的鲁棒性。现有方法缺乏对不同LLM在相同攻击下的鲁棒性差异的系统性评估，难以有效指导防御策略的开发。BERT等模型容易受到对抗攻击的影响，导致性能显著下降，这在实际应用中构成安全隐患。

**核心思路**：论文的核心思路是通过系统设计的对抗性攻击，评估不同LLM（Flan-T5、BERT和RoBERTa-Base）在面对这些攻击时的性能表现。通过对比不同模型的表现，揭示其内在的鲁棒性差异，从而为开发更有效的防御策略提供依据。这种方法侧重于实证分析，而非理论推导，更贴近实际应用场景。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 选择目标LLM：选取Flan-T5、BERT和RoBERTa-Base作为研究对象。2) 设计对抗性攻击：使用TextFooler和BERTAttack两种攻击方法生成对抗样本。3) 评估模型性能：在原始样本和对抗样本上分别测试LLM的准确率。4) 分析结果：对比不同模型在不同攻击下的性能下降情况，评估其鲁棒性。

**关键创新**：论文的关键创新在于对不同LLM的鲁棒性进行了差异化评估，揭示了不同模型在面对相同对抗攻击时的性能差异。以往的研究可能更侧重于开发新的攻击方法或防御策略，而该论文则侧重于对现有模型的鲁棒性进行深入分析，为后续研究提供了重要的参考。

**关键设计**：论文的关键设计在于选择了TextFooler和BERTAttack两种不同的对抗攻击方法。TextFooler是一种基于梯度的攻击方法，通过修改文本中的词语来欺骗模型。BERTAttack则是一种基于BERT的攻击方法，通过生成与原始文本相似但语义不同的文本来攻击模型。选择这两种不同的攻击方法可以更全面地评估模型的鲁棒性。

## 📊 实验亮点

实验结果表明，RoBERTa-Base和FlanT5在对抗攻击下表现出极高的鲁棒性，攻击成功率为0%。相比之下，BERT-Base则非常脆弱，TextFooler攻击成功率高达93.75%，导致其准确率从48%大幅下降至3%。这些数据清晰地展示了不同模型在鲁棒性方面的巨大差异。

## 🎯 应用场景

该研究成果可应用于提升自然语言处理系统的安全性，尤其是在金融、医疗等对安全性要求较高的领域。通过了解不同模型的鲁棒性，可以选择更安全的模型或针对性地开发防御策略，降低对抗攻击带来的风险。此外，该研究也为未来开发更鲁棒的LLM提供了指导。

## 📄 摘要（原文）

> This study evaluates the resilience of large language models (LLMs) against adversarial attacks, specifically focusing on Flan-T5, BERT, and RoBERTa-Base. Using systematically designed adversarial tests through TextFooler and BERTAttack, we found significant variations in model robustness. RoBERTa-Base and FlanT5 demonstrated remarkable resilience, maintaining accuracy even when subjected to sophisticated attacks, with attack success rates of 0%. In contrast. BERT-Base showed considerable vulnerability, with TextFooler achieving a 93.75% success rate in reducing model accuracy from 48% to just 3%. Our research reveals that while certain LLMs have developed effective defensive mechanisms, these safeguards often require substantial computational resources. This study contributes to the understanding of LLM security by identifying existing strengths and weaknesses in current safeguarding approaches and proposes practical recommendations for developing more efficient and effective defensive strategies.

