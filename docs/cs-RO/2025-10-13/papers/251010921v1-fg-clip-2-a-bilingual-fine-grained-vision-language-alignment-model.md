---
layout: default
title: FG-CLIP 2: A Bilingual Fine-grained Vision-Language Alignment Model
---

# FG-CLIP 2: A Bilingual Fine-grained Vision-Language Alignment Model

**arXiv**: [2510.10921v1](https://arxiv.org/abs/2510.10921) | [PDF](https://arxiv.org/pdf/2510.10921.pdf)

**作者**: Chunyu Xie, Bin Wang, Fanjing Kong, Jincheng Li, Dawei Liang, Ji Ao, Dawei Leng, Yuhui Yin

---

## 💡 一句话要点

**提出FG-CLIP 2模型以解决双语细粒度视觉-语言对齐问题**

**关键词**: `细粒度视觉-语言对齐` `双语模型` `区域-文本匹配` `长字幕建模` `TIC损失` `多模态基准`

## 📋 核心要点

1. 核心问题：现有模型在细粒度视觉-语言对齐上表现不足，尤其在非英语场景。
2. 方法要点：采用区域-文本匹配、长字幕建模及TIC损失，提升双语细粒度对齐。
3. 实验或效果：在29个数据集上超越现有方法，实现双语最先进性能。

## 📄 摘要（原文）

> Fine-grained vision-language understanding requires precise alignment between
> visual content and linguistic descriptions, a capability that remains limited
> in current models, particularly in non-English settings. While models like CLIP
> perform well on global alignment, they often struggle to capture fine-grained
> details in object attributes, spatial relations, and linguistic expressions,
> with limited support for bilingual comprehension. To address these challenges,
> we introduce FG-CLIP 2, a bilingual vision-language model designed to advance
> fine-grained alignment for both English and Chinese. Our approach leverages
> rich fine-grained supervision, including region-text matching and long-caption
> modeling, alongside multiple discriminative objectives. We further introduce
> the Textual Intra-modal Contrastive (TIC) loss to better distinguish
> semantically similar captions. Trained on a carefully curated mixture of
> large-scale English and Chinese data, FG-CLIP 2 achieves powerful bilingual
> performance. To enable rigorous evaluation, we present a new benchmark for
> Chinese multimodal understanding, featuring long-caption retrieval and bounding
> box classification. Extensive experiments on 29 datasets across 8 tasks show
> that FG-CLIP 2 outperforms existing methods, achieving state-of-the-art results
> in both languages. We release the model, code, and benchmark to facilitate
> future research on bilingual fine-grained alignment.

