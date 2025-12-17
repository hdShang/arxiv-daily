---
layout: default
title: DeepSeek-OCR: Contexts Optical Compression
---

# DeepSeek-OCR: Contexts Optical Compression

**arXiv**: [2510.18234v1](https://arxiv.org/abs/2510.18234) | [PDF](https://arxiv.org/pdf/2510.18234.pdf)

**作者**: Haoran Wei, Yaofeng Sun, Yukun Li

---

## 💡 一句话要点

**提出DeepSeek-OCR以压缩长上下文光学映射，实现高效OCR解码。**

**关键词**: `光学字符识别` `上下文压缩` `视觉令牌优化` `长文档处理` `模型解码`

## 📋 核心要点

1. 核心问题：长上下文光学压缩的可行性，减少视觉令牌数以优化处理。
2. 方法要点：使用DeepEncoder和DeepSeek3B-MoE-A570M解码器，实现高压缩比和低激活。
3. 实验效果：压缩比<10x时OCR精度达97%，20x时约60%，在基准测试中超越现有模型。

## 📄 摘要（原文）

> We present DeepSeek-OCR as an initial investigation into the feasibility of
> compressing long contexts via optical 2D mapping. DeepSeek-OCR consists of two
> components: DeepEncoder and DeepSeek3B-MoE-A570M as the decoder. Specifically,
> DeepEncoder serves as the core engine, designed to maintain low activations
> under high-resolution input while achieving high compression ratios to ensure
> an optimal and manageable number of vision tokens. Experiments show that when
> the number of text tokens is within 10 times that of vision tokens (i.e., a
> compression ratio < 10x), the model can achieve decoding (OCR) precision of
> 97%. Even at a compression ratio of 20x, the OCR accuracy still remains at
> about 60%. This shows considerable promise for research areas such as
> historical long-context compression and memory forgetting mechanisms in LLMs.
> Beyond this, DeepSeek-OCR also demonstrates high practical value. On
> OmniDocBench, it surpasses GOT-OCR2.0 (256 tokens/page) using only 100 vision
> tokens, and outperforms MinerU2.0 (6000+ tokens per page on average) while
> utilizing fewer than 800 vision tokens. In production, DeepSeek-OCR can
> generate training data for LLMs/VLMs at a scale of 200k+ pages per day (a
> single A100-40G). Codes and model weights are publicly accessible at
> http://github.com/deepseek-ai/DeepSeek-OCR.

