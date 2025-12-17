---
layout: default
title: Safe2Harm: Semantic Isomorphism Attacks for Jailbreaking Large Language Models
---

# Safe2Harm: Semantic Isomorphism Attacks for Jailbreaking Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13703" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13703</a>
  <a href="https://arxiv.org/pdf/2512.13703.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13703" onclick="toggleFavorite(this, '2512.13703', 'Safe2Harm: Semantic Isomorphism Attacks for Jailbreaking Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fan Yang

**分类**: cs.CR, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出Safe2Harm语义同构攻击，实现对大型语言模型的有效越狱**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `越狱攻击` `语义同构` `安全漏洞` `有害内容检测`

## 📋 核心要点

1. 现有LLM越狱方法主要依赖提示工程或对抗优化，忽略了有害场景与合法场景在底层原理上的相似性。
2. Safe2Harm攻击通过将有害问题转化为语义安全的同构问题，利用LLM对安全问题的回答，再反向映射生成有害内容。
3. 实验证明Safe2Harm在多个LLM上表现出强大的越狱能力，优于现有方法，并构建了新的有害内容评估数据集。

## 📝 摘要（中文）

大型语言模型（LLMs）在各种任务中表现出卓越的性能，但其安全漏洞可能被攻击者利用以生成有害内容，从而对各个社会领域造成不利影响。现有的大多数越狱方法都围绕提示工程或对抗优化展开，但我们发现了一个先前被忽视的现象：许多有害场景在底层原理上与合法场景高度一致。基于这一发现，本文提出了一种Safe2Harm语义同构攻击方法，该方法通过四个阶段实现高效的越狱：首先，将有害问题重写为语义上安全的、具有相似底层原理的问题；其次，提取两者之间的主题映射关系；第三，让LLM生成针对安全问题的详细回答；最后，基于主题映射关系反向重写安全回答，以获得有害输出。在7个主流LLM和三种类型的基准数据集上的实验表明，Safe2Harm表现出强大的越狱能力，其整体性能优于现有方法。此外，我们构建了一个包含358个样本的具有挑战性的有害内容评估数据集，并评估了现有有害检测方法的有效性，这些方法可以部署用于LLM输入输出过滤，以实现防御。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）容易被越狱，从而生成有害内容的问题。现有的越狱方法，如提示工程和对抗优化，存在效率低、泛化性差等痛点，并且忽略了有害场景与合法场景在底层原理上的相似性，导致攻击效果不佳。

**核心思路**：论文的核心思路是利用语义同构性，将有害问题转化为语义上安全的、但底层原理相似的问题，诱导LLM生成针对安全问题的回答，然后通过反向映射将安全回答转化为有害输出。这种方法旨在绕过LLM的安全机制，利用其在安全问题上的生成能力，间接生成有害内容。

**技术框架**：Safe2Harm攻击方法包含四个主要阶段：
1. **问题重写**：将有害问题重写为语义安全的同构问题。
2. **主题映射**：提取有害问题和安全问题之间的主题映射关系。
3. **安全回答生成**：利用LLM生成针对安全问题的详细回答。
4. **反向重写**：基于主题映射关系，将安全回答反向重写为有害输出。

**关键创新**：Safe2Harm的关键创新在于发现了并利用了有害场景与合法场景之间的语义同构性。与直接攻击LLM的安全机制不同，Safe2Harm通过转换问题，绕过了安全检测，利用了LLM在安全问题上的生成能力。这种间接攻击方式更具隐蔽性和有效性。

**关键设计**：论文的关键设计包括：
1. **语义安全问题生成策略**：如何将有害问题转化为语义安全的同构问题，保证底层原理相似，但表面上无害。
2. **主题映射关系提取方法**：如何准确提取有害问题和安全问题之间的主题映射关系，保证反向重写的准确性。
3. **反向重写策略**：如何基于主题映射关系，将安全回答准确地转化为有害输出，避免引入新的安全风险。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13703/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13703/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13703/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Safe2Harm在7个主流LLM和三种类型的基准数据集上进行了实验，结果表明其越狱能力优于现有方法。此外，论文构建了一个包含358个样本的具有挑战性的有害内容评估数据集，并评估了现有有害检测方法的有效性，为LLM的安全防御提供了新的思路。

## 🎯 应用场景

该研究成果可应用于提升大型语言模型的安全性评估，通过Safe2Harm攻击方法发现LLM潜在的安全漏洞。同时，构建的有害内容评估数据集可用于训练和评估LLM的有害内容检测能力，从而提高LLM的安全性，减少有害内容的生成和传播。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated exceptional performance across various tasks, but their security vulnerabilities can be exploited by attackers to generate harmful content, causing adverse impacts across various societal domains. Most existing jailbreak methods revolve around Prompt Engineering or adversarial optimization, yet we identify a previously overlooked phenomenon: many harmful scenarios are highly consistent with legitimate ones in terms of underlying principles. Based on this finding, this paper proposes the Safe2Harm Semantic Isomorphism Attack method, which achieves efficient jailbreaking through four stages: first, rewrite the harmful question into a semantically safe question with similar underlying principles; second, extract the thematic mapping relationship between the two; third, let the LLM generate a detailed response targeting the safe question; finally, reversely rewrite the safe response based on the thematic mapping relationship to obtain harmful output. Experiments on 7 mainstream LLMs and three types of benchmark datasets show that Safe2Harm exhibits strong jailbreaking capability, and its overall performance is superior to existing methods. Additionally, we construct a challenging harmful content evaluation dataset containing 358 samples and evaluate the effectiveness of existing harmful detection methods, which can be deployed for LLM input-output filtering to enable defense.

