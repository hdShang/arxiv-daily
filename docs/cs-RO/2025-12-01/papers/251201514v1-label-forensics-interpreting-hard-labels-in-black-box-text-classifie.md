---
layout: default
title: Label Forensics: Interpreting Hard Labels in Black-Box Text Classifier
---

# Label Forensics: Interpreting Hard Labels in Black-Box Text Classifier

**arXiv**: [2512.01514v1](https://arxiv.org/abs/2512.01514) | [PDF](https://arxiv.org/pdf/2512.01514.pdf)

**作者**: Mengyao Du, Gang Yang, Han Fang, Quanjun Yin, Ee-chien Chang

---

## 💡 一句话要点

**提出标签取证框架以解释黑盒文本分类器的硬标签语义**

**关键词**: `黑盒分类器` `标签语义解释` `文本分类` `AI审计` `句子嵌入分布`

## 📋 核心要点

1. 核心问题：黑盒文本分类器仅输出硬标签，其内部语义未知，引发审计与取证担忧。
2. 方法要点：通过语义邻域采样和迭代优化，构建句子嵌入分布来重构标签的语义概念。
3. 实验或效果：在多个黑盒分类器上平均标签一致性达92.24%，验证了语义捕获的准确性。

## 📄 摘要（原文）

> The widespread adoption of natural language processing techniques has led to an unprecedented growth of text classifiers across the modern web. Yet many of these models circulate with their internal semantics undocumented or even intentionally withheld. Such opaque classifiers, which may expose only hard-label outputs, can operate in unregulated web environments or be repurposed for unknown intents, raising legitimate forensic and auditing concerns. In this paper, we position ourselves as investigators and work to infer the semantic concept each label encodes in an undocumented black-box classifier.
>   Specifically, we introduce label forensics, a black-box framework that reconstructs a label's semantic meaning. Concretely, we represent a label by a sentence embedding distribution from which any sample reliably reflects the concept the classifier has implicitly learned for that label. We believe this distribution should maintain two key properties: precise, with samples consistently classified into the target label, and general, covering the label's broad semantic space. To realize this, we design a semantic neighborhood sampler and an iterative optimization procedure to select representative seed sentences that jointly maximize label consistency and distributional coverage. The final output, an optimized seed sentence set combined with the sampler, constitutes the empirical distribution representing the label's semantics. Experiments on multiple black-box classifiers achieve an average label consistency of around 92.24 percent, demonstrating that the embedding regions accurately capture each classifier's label semantics. We further validate our framework on an undocumented HuggingFace classifier, enabling fine-grained label interpretation and supporting responsible AI auditing.

