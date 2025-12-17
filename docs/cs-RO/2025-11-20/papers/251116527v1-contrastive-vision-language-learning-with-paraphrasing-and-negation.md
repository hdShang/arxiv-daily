---
layout: default
title: Contrastive vision-language learning with paraphrasing and negation
---

# Contrastive vision-language learning with paraphrasing and negation

**arXiv**: [2511.16527v1](https://arxiv.org/abs/2511.16527) | [PDF](https://arxiv.org/pdf/2511.16527.pdf)

**作者**: Kwun Ho Ngan, Saman Sadeghi Afgeh, Joe Townsend, Artur d'Avila Garcez

---

## 💡 一句话要点

**提出SemCLIP以增强视觉语言模型对语义变换的鲁棒性**

**关键词**: `对比学习` `视觉语言模型` `语义鲁棒性` `否定处理` `转述处理` `零样本分类`

## 📋 核心要点

1. 核心问题：CLIP模型在否定和转述文本上表现不稳定，影响图像检索准确性。
2. 方法要点：引入新对比损失函数，结合LLM生成原始、转述和否定文本三元组进行训练。
3. 实验或效果：在CC-Neg基准上，图像检索准确率从68.1%提升至78.1%。

## 📄 摘要（原文）

> Contrastive vision-language models continue to be the dominant approach for image and text retrieval. Contrastive Language-Image Pre-training (CLIP) trains two neural networks in contrastive manner to align their image and text embeddings in a shared latent space. Recent results evaluating CLIP on negated or paraphrased text have shown mixed performance because negation changes meaning radically with minimal lexical changes, while paraphrasing can create very different textual expressions with the same intended meaning. This poses a significant challenge for improving the evaluation results and alignment of vision-language models. To address this challenge, this paper evaluates the combination of paraphrasing and negation, proposes a new CLIP contrastive loss function accounting for both paraphrasing and negation, and applies LLM-generated training triples consisting of original, paraphrased and negated textual captions to CLIP-like training models. The approach, called SemCLIP, is shown to move paraphrased captions towards the original image embeddings while pushing negated captions further away in embedding space. Empirically, SemCLIP is shown to be capable of preserving CLIP's performance while increasing considerably the distances to negated captions. On the CC-Neg benchmark using an original over negation image-retrieval accuracy metric, SemCLIP improves accuracy from 68.1% to 78.1%. Although results are mixed when compared with CLIP on the Sugarcrepe++ benchmark, SemCLIP's performance is generally better than the models trained with negated captions. This robustness to negation extends to downstream zero-shot classification tasks where SemCLIP pre-trained on Sugarcrepe++ performs better than CLIP on all tested downstream tasks. These results indicate that SemCLIP can achieve significant robustness to semantic transformations.

