---
layout: default
title: Towards Mitigating Hallucinations in Large Vision-Language Models by Refining Textual Embeddings
---

# Towards Mitigating Hallucinations in Large Vision-Language Models by Refining Textual Embeddings

**arXiv**: [2511.05017v1](https://arxiv.org/abs/2511.05017) | [PDF](https://arxiv.org/pdf/2511.05017.pdf)

**作者**: Aakriti Agrawal, Gouthaman KV, Rohith Aralikatti, Gauri Jagatap, Jiaxin Yuan, Vijay Kamarshi, Andrea Fanelli, Furong Huang

---

## 💡 一句话要点

**提出通过精炼文本嵌入来缓解大型视觉语言模型中的幻觉问题**

**关键词**: `大型视觉语言模型` `幻觉缓解` `文本嵌入精炼` `视觉特征融合` `模态不平衡` `视觉接地`

## 📋 核心要点

1. 核心问题：现有LVLM架构偏向语言模态，导致视觉幻觉
2. 方法要点：使用平均池化视觉特征精炼文本嵌入，增强视觉基础
3. 实验或效果：在基准测试中显著减少幻觉，提升视觉接地能力

## 📄 摘要（原文）

> In this work, we identify an inherent bias in prevailing LVLM architectures
> toward the language modality, largely resulting from the common practice of
> simply appending visual embeddings to the input text sequence. To address this,
> we propose a simple yet effective method that refines textual embeddings by
> integrating average-pooled visual features. Our approach demonstrably improves
> visual grounding and significantly reduces hallucinations on established
> benchmarks. While average pooling offers a straightforward, robust, and
> efficient means of incorporating visual information, we believe that more
> sophisticated fusion methods could further enhance visual grounding and
> cross-modal alignment. Given that the primary focus of this work is to
> highlight the modality imbalance and its impact on hallucinations -- and to
> show that refining textual embeddings with visual information mitigates this
> issue -- we leave exploration of advanced fusion strategies for future work.

