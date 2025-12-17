---
layout: default
title: Large Speech Model Enabled Semantic Communication
---

# Large Speech Model Enabled Semantic Communication

**arXiv**: [2512.04711v1](https://arxiv.org/abs/2512.04711) | [PDF](https://arxiv.org/pdf/2512.04711.pdf)

**作者**: Yun Tian, Zhijin Qin, Guocheng Lv, Ye Jin, Kaibin Huang, Zhu Han

---

## 💡 一句话要点

**提出基于大型语音模型的语义通信系统，实现自适应压缩与鲁棒传输**

**关键词**: `语义通信` `大型语音模型` `自适应传输` `不等错误保护` `低秩适应` `实时部署`

## 📋 核心要点

1. 现有语音语义通信系统受限于特定任务设计，性能有限
2. 采用Mimi语音编解码器与自适应控制器，支持带宽自适应与不等错误保护
3. 仿真显示系统在550 bps至2.06 kbps带宽下，高丢包率时语音质量优于基线，延迟约460 ms

## 📄 摘要（原文）

> Existing speech semantic communication systems mainly based on Joint Source-Channel Coding (JSCC) architectures have demonstrated impressive performance, but their effectiveness remains limited by model structures specifically designed for particular tasks and datasets. Recent advances indicate that generative large models pre-trained on massive datasets, can achieve outstanding performance arexhibit exceptional performance across diverse downstream tasks with minimal fine-tuning. To exploit the rich semantic knowledge embedded in large models and enable adaptive transmission over lossy channels, we propose a Large Speech Model enabled Semantic Communication (LargeSC) system. Simultaneously achieving adaptive compression and robust transmission over lossy channels remains challenging, requiring trade-offs among compression efficiency, speech quality, and latency. In this work, we employ the Mimi as a speech codec, converting speech into discrete tokens compatible with existing network architectures. We propose an adaptive controller module that enables adaptive transmission and in-band Unequal Error Protection (UEP), dynamically adjusting to both speech content and packet loss probability under bandwidth constraints. Additionally, we employ Low-Rank Adaptation (LoRA) to finetune the Moshi foundation model for generative recovery of lost speech tokens. Simulation results show that the proposed system supports bandwidths ranging from 550 bps to 2.06 kbps, outperforms conventional baselines in speech quality under high packet loss rates and achieves an end-to-end latency of approximately 460 ms, thereby demonstrating its potential for real-time deployment.

