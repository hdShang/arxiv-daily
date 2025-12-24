---
layout: default
title: "ZKPROV: A Zero-Knowledge Approach to Dataset Provenance for Large Language Models"
---

# ZKPROV: A Zero-Knowledge Approach to Dataset Provenance for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20915" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20915v2</a>
  <a href="https://arxiv.org/pdf/2506.20915.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20915v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20915v2', 'ZKPROV: A Zero-Knowledge Approach to Dataset Provenance for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mina Namazi, Alexander Nemecek, Erman Ayday

**分类**: cs.CR, cs.AI, cs.LG

**发布日期**: 2025-06-26 (更新: 2025-12-18)

**备注**: 16 pages, 3 figures

---

## 💡 一句话要点

**提出ZKPROV以解决大语言模型数据来源验证问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `数据来源验证` `零知识证明` `数据隐私` `密码学框架` `敏感领域应用` `合规性`

## 📋 核心要点

1. 现有方法在验证大语言模型的计算来源时面临高昂的计算成本或信息泄露的风险。
2. ZKPROV通过零知识证明技术，允许用户验证模型响应的训练数据集来源，同时保护数据隐私。
3. 实验结果显示，ZKPROV在生成和验证证明时具有亚线性扩展性，处理时间低于3.3秒，适用于实际应用。

## 📝 摘要（中文）

随着大语言模型（LLMs）在敏感领域的应用，准确验证其计算来源而不泄露训练数据集成为一项重大挑战，尤其是在医疗等受监管行业。传统方法要么需要高昂的计算成本来完全验证整个训练过程，要么会向验证者泄露未授权的信息。因此，本文提出了ZKPROV，这是一种新颖的密码学框架，允许用户验证LLM对其提示的响应是基于由数据集所有者认证的数据集进行训练的。此外，它确保数据集内容与用户查询相关，同时不泄露敏感信息。ZKPROV在隐私与效率之间提供了独特的平衡，通过将训练数据集、模型参数和响应绑定在一起，并附加零知识证明来验证这些声明。实验结果表明，对于最大参数量为8B的模型，生成和验证这些证明的端到端开销低于3.3秒，展示了其在实际应用中的可行性。

## 🔬 方法详解

**问题定义**：本文旨在解决在敏感领域中验证大语言模型（LLMs）计算来源的问题，现有方法往往需要高昂的计算成本或会泄露敏感信息。

**核心思路**：ZKPROV通过引入零知识证明技术，允许用户在不泄露训练数据集内容的情况下，验证模型响应的来源和相关性。这样的设计确保了数据隐私，同时满足了合规性要求。

**技术框架**：ZKPROV的整体架构包括数据集认证、模型参数绑定和响应生成三个主要模块。用户提交查询后，系统生成相应的零知识证明，确保数据集的合法性和相关性。

**关键创新**：ZKPROV的主要创新在于将训练数据集、模型参数和生成响应绑定在一起，并通过零知识证明验证这些绑定的有效性。这与传统方法的显著区别在于，它不需要泄露任何敏感信息。

**关键设计**：在实现中，ZKPROV采用了高效的零知识证明算法，确保生成和验证过程的时间复杂度保持在亚线性水平。此外，系统设计了合理的参数设置，以优化性能和安全性。

## 📊 实验亮点

实验结果表明，ZKPROV在生成和验证零知识证明时具有亚线性扩展性，处理时间低于3.3秒，适用于最大参数量为8B的模型。这一性能显著优于传统方法，展示了其在实际应用中的可行性和效率。

## 🎯 应用场景

ZKPROV的潜在应用领域包括医疗、金融和法律等受监管行业，这些领域对数据来源的验证有严格要求。通过确保数据集的合法性和相关性，ZKPROV可以帮助企业在合规的同时，利用大语言模型进行创新和决策。未来，该技术可能推动更多行业在数据隐私和安全性方面的进步。

## 📄 摘要（原文）

> As large language models (LLMs) are used in sensitive fields, accurately verifying their computational provenance without disclosing their training datasets poses a significant challenge, particularly in regulated sectors such as healthcare, which have strict requirements for dataset use. Traditional approaches either incur substantial computational cost to fully verify the entire training process or leak unauthorized information to the verifier. Therefore, we introduce ZKPROV, a novel cryptographic framework allowing users to verify that the LLM's responses to their prompts are trained on datasets certified by the authorities that own them. Additionally, it ensures that the dataset's content is relevant to the users' queries without revealing sensitive information about the datasets or the model parameters. ZKPROV offers a unique balance between privacy and efficiency by binding training datasets, model parameters, and responses, while also attaching zero-knowledge proofs to the responses generated by the LLM to validate these claims. Our experimental results demonstrate sublinear scaling for generating and verifying these proofs, with end-to-end overhead under 3.3 seconds for models up to 8B parameters, presenting a practical solution for real-world applications. We also provide formal security guarantees, proving that our approach preserves dataset confidentiality while ensuring trustworthy dataset provenance.

