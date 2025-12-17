---
layout: default
title: Adapting Neural Audio Codecs to EEG
---

# Adapting Neural Audio Codecs to EEG

**arXiv**: [2511.23142v1](https://arxiv.org/abs/2511.23142) | [PDF](https://arxiv.org/pdf/2511.23142.pdf)

**作者**: Ard Kastrati, Luca Lanzendörfer, Riccardo Rigoni, John Staib Matilla, Roger Wattenhofer

---

## 💡 一句话要点

**提出基于神经音频编解码器的EEG压缩方法，通过预处理和微调实现高效重建**

**关键词**: `EEG压缩` `神经音频编解码器` `多通道扩展` `预处理适配` `微调优化` `临床信息保留`

## 📋 核心要点

1. 核心问题：EEG与音频在采样率、通道结构和尺度上差异大，需适配神经音频编解码器进行压缩
2. 方法要点：使用DAC作为基础，预处理EEG数据以匹配编解码器输入，提出多通道扩展DAC-MC以捕获空间依赖
3. 实验或效果：在TUH数据集上评估，显示方法保留临床相关信息，提升重建质量和下游分类精度

## 📄 摘要（原文）

> EEG and audio are inherently distinct modalities, differing in sampling rate, channel structure, and scale. Yet, we show that pretrained neural audio codecs can serve as effective starting points for EEG compression, provided that the data are preprocessed to be suitable to the codec's input constraints. Using DAC, a state-of-the-art neural audio codec as our base, we demonstrate that raw EEG can be mapped into the codec's stride-based framing, enabling direct reuse of the audio-pretrained encoder-decoder. Even without modification, this setup yields stable EEG reconstructions, and fine-tuning on EEG data further improves fidelity and generalization compared to training from scratch. We systematically explore compression-quality trade-offs by varying residual codebook depth, codebook (vocabulary) size, and input sampling rate. To capture spatial dependencies across electrodes, we propose DAC-MC, a multi-channel extension with attention-based cross-channel aggregation and channel-specific decoding, while retaining the audio-pretrained initialization. Evaluations on the TUH Abnormal and Epilepsy datasets show that the adapted codecs preserve clinically relevant information, as reflected in spectrogram-based reconstruction loss and downstream classification accuracy.

