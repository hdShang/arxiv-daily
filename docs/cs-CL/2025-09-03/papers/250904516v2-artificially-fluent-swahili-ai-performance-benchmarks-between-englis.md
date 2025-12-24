---
layout: default
title: "Artificially Fluent: Swahili AI Performance Benchmarks Between English-Trained and Natively-Trained Datasets"
---

# Artificially Fluent: Swahili AI Performance Benchmarks Between English-Trained and Natively-Trained Datasets

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04516" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04516v2</a>
  <a href="https://arxiv.org/pdf/2509.04516.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04516v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04516v2', 'Artificially Fluent: Swahili AI Performance Benchmarks Between English-Trained and Natively-Trained Datasets')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sophie Jaffer, Simeon Sayer

**分类**: cs.CL, cs.CY

**发布日期**: 2025-09-03 (更新: 2025-09-28)

**备注**: 13 Pages, 3 Figures

---

## 💡 一句话要点

**对比英语训练与斯瓦希里语原生训练，揭示LLM跨语言性能差异**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言模型` `语言公平性` `斯瓦希里语` `BERT模型` `跨语言迁移` `自然语言处理` `机器翻译` `性能评估`

## 📋 核心要点

1. 大型语言模型在多语言处理中存在性能差异，英语数据主导地位可能导致非英语使用者处于劣势。
2. 通过对比英语训练和斯瓦希里语原生训练的BERT模型，研究语言一致性与跨语言抽象对模型性能的影响。
3. 实验结果表明，原生斯瓦希里语训练模型优于翻译后的英语模型，揭示了翻译无法完全弥合语言表征差异。

## 📝 摘要（中文）

随着大型语言模型(LLM)多语言能力的扩展，其在不同语言上的性能公平性问题日益突出。为了验证数据差异可能影响模型性能的假设，本研究比较了两个单语BERT模型：一个完全在斯瓦希里语数据上训练和测试，另一个在可比的英语新闻数据上训练和测试。为了模拟多语言LLM如何通过内部翻译和抽象处理非英语查询，我们将斯瓦希里语新闻数据翻译成英语，并使用英语训练的模型进行评估。通过比较在英语模型上评估斯瓦希里语翻译输入的性能，与完全在斯瓦希里语中训练和测试模型的性能，从而分离语言一致性与跨语言抽象的影响。结果表明，尽管翻译质量很高，但原生斯瓦希里语训练的模型表现优于斯瓦希里语到英语翻译的模型，错误率分别0.36%和1.47%，前者错误率约为后者的四分之一。这表明翻译本身并不能弥合语言之间的表征差异，并且在一种语言中训练的模型可能难以准确解释翻译后的输入，因为其内部知识表示不完善。因此，对于可靠的结果，母语训练仍然很重要。未来的研究应侧重于为代表性不足的语言开发更广泛的数据集，并重新关注多语言模型评估，确保全球人工智能部署对现有数字鸿沟的强化效应得以降低。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在处理不同语言时存在的性能差异问题。现有方法，特别是依赖于英语数据训练的模型，在处理非英语语言时可能表现不佳，因为它们无法充分理解和表示这些语言的细微差别。这种性能差距可能会加剧数字鸿沟，使非英语使用者在获取信息和教育资源方面处于不利地位。

**核心思路**：论文的核心思路是通过对比在原生语言（斯瓦希里语）上训练的模型和将斯瓦希里语翻译成英语后在英语模型上评估的模型，来评估语言一致性和跨语言抽象对模型性能的影响。通过这种方式，可以分离出语言本身对模型性能的影响，并探讨翻译是否能够弥合语言之间的表征差异。

**技术框架**：论文采用了一种对比实验的设计。首先，使用斯瓦希里语新闻数据训练一个单语BERT模型。然后，将相同的斯瓦希里语新闻数据翻译成英语，并使用英语新闻数据训练另一个单语BERT模型。最后，使用原始斯瓦希里语数据和翻译后的英语数据分别对两个模型进行评估。通过比较两个模型的性能，可以评估语言一致性和跨语言抽象对模型性能的影响。

**关键创新**：论文的关键创新在于其评估方法，即通过翻译非英语数据并在英语模型上进行评估，来模拟多语言LLM处理非英语查询的过程。这种方法能够有效地分离出语言本身对模型性能的影响，并探讨翻译是否能够弥合语言之间的表征差异。此外，论文还关注了代表性不足的语言（斯瓦希里语），这有助于提高人们对多语言模型性能公平性的认识。

**关键设计**：论文使用了BERT模型作为基础模型，并采用了标准的新闻数据作为训练和测试数据。关键的参数设置包括BERT模型的超参数（如学习率、批大小等）以及翻译模型的质量。损失函数采用标准的交叉熵损失函数。网络结构为标准的BERT结构。

## 📊 实验亮点

实验结果表明，原生斯瓦希里语训练的BERT模型错误率为0.36%，而斯瓦希里语翻译成英语后在英语模型上评估的错误率为1.47%。原生模型错误率约为翻译模型的四分之一，显著优于翻译后的模型，表明语言一致性对模型性能至关重要。

## 🎯 应用场景

该研究成果可应用于提升多语言环境下人工智能系统的性能，尤其是在教育、信息检索等领域。通过关注代表性不足的语言，有助于缩小数字鸿沟，促进全球范围内更公平的人工智能应用。未来的研究可以进一步探索如何利用迁移学习、多语言训练等技术，提高模型在各种语言上的性能。

## 📄 摘要（原文）

> As large language models (LLMs) expand multilingual capabilities, questions remain about the equity of their performance across languages. While many communities stand to benefit from AI systems, the dominance of English in training data risks disadvantaging non-English speakers. To test the hypothesis that such data disparities may affect model performance, this study compares two monolingual BERT models: one trained and tested entirely on Swahili data, and another on comparable English news data. To simulate how multilingual LLMs process non-English queries through internal translation and abstraction, we translated the Swahili news data into English and evaluated it using the English-trained model. This approach tests the hypothesis by evaluating whether translating Swahili inputs for evaluation on an English model yields better or worse performance compared to training and testing a model entirely in Swahili, thus isolating the effect of language consistency versus cross-lingual abstraction. The results prove that, despite high-quality translation, the native Swahili-trained model performed better than the Swahili-to-English translated model, producing nearly four times fewer errors: 0.36% vs. 1.47% respectively. This gap suggests that translation alone does not bridge representational differences between languages and that models trained in one language may struggle to accurately interpret translated inputs due to imperfect internal knowledge representation, suggesting that native-language training remains important for reliable outcomes. In educational and informational contexts, even small performance gaps may compound inequality. Future research should focus on addressing broader dataset development for underrepresented languages and renewed attention to multilingual model evaluation, ensuring the reinforcing effect of global AI deployment on existing digital divides is reduced.

