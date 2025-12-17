---
layout: default
title: DUO-TOK: Dual-Track Semantic Music Tokenizer for Vocal-Accompaniment Generation
---

# DUO-TOK: Dual-Track Semantic Music Tokenizer for Vocal-Accompaniment Generation

**arXiv**: [2511.20224v1](https://arxiv.org/abs/2511.20224) | [PDF](https://arxiv.org/pdf/2511.20224.pdf)

**作者**: Rui Lin, Zhiyue Wu, Jiahe Le, Kangdi Wang, Weixiong Chen, Junyu Dai, Tao Jiang

---

## 💡 一句话要点

**提出DUO-TOK双轨语义音乐分词器，解决歌词到歌曲生成中重建质量与语言模型可学习性间的权衡问题。**

**关键词**: `音乐分词器` `双轨结构` `自监督学习` `潜在扩散模型` `歌词到歌曲生成`

## 📋 核心要点

1. 核心问题：现有音乐编解码器在重建保真度与语言模型友好性间存在权衡，且缺乏对声乐-伴奏双轨结构的感知。
2. 方法要点：采用四阶段自监督学习流程，包括预训练编码器、表示稳定与因子化、学习双码本和训练潜在扩散解码器。
3. 实验或效果：在0.75 kbps下，优化重建-生成帕累托前沿，实现最佳音乐标签AP和最低词汇归一化LM困惑度。

## 📄 摘要（原文）

> Duo-Tok is a source-aware dual-codebook tokenizer for vocal-accompaniment music that targets the growing tension between reconstruction quality and language-model (LM) learnability in modern lyrics-to-song systems. Existing codecs either prioritize high-fidelity reconstruction with difficult-to-model acoustic tokens or compress aggressively into semantic tokens that are LM-friendly but lossy, and they rarely make the tokenizer itself aware of dual-track structure. Duo-Tok follows a four-stage, SSL-centered pipeline: we first pretrain a BEST-RQ-style encoder on large-scale audio, then stabilize and factorize the representation with Gaussian replacement noise and multi-task supervision, before freezing the encoder to learn SimVQ-based dual codebooks with hard routing for vocals and accompaniment, and finally training latent diffusion decoders on top of the discrete tokens. Duo-Tok at 0.75 kbps shifts the empirical reconstruction-generation Pareto frontier, achieving the best music-tagging AP and the lowest vocabulary-normalized LM perplexity among compared codecs while maintaining reconstruction quality comparable to state-of-the-art music tokenizers.

