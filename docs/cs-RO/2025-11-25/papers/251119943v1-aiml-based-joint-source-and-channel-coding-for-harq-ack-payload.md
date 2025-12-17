---
layout: default
title: AI/ML based Joint Source and Channel Coding for HARQ-ACK Payload
---

# AI/ML based Joint Source and Channel Coding for HARQ-ACK Payload

**arXiv**: [2511.19943v1](https://arxiv.org/abs/2511.19943) | [PDF](https://arxiv.org/pdf/2511.19943.pdf)

**作者**: Akash Doshi, Pinar Sen, Kirill Ivanov, Wei Yang, June Namgoong, Runxin Wang, Rachel Wang, Taesang Yoo, Jing Jiang, Tingfang Ji

---

## 💡 一句话要点

**提出基于Transformer的联合信源信道编码以优化HARQ-ACK传输**

**关键词**: `联合信源信道编码` `HARQ-ACK传输` `Transformer编码器` `不等错误保护` `5G新空口` `深度学习训练`

## 📋 核心要点

1. HARQ-ACK比特非均匀分布，传统信道编码假设均匀分布导致性能损失
2. 采用Transformer编码器和自由午餐训练算法，结合功率整形和不等错误保护
3. 在5G NR上行链路中实现3-6 dB平均功率降低和2-3 dB峰值功率降低

## 📄 摘要（原文）

> Channel coding from 2G to 5G has assumed the inputs bits at the physical layer to be uniformly distributed. However, hybrid automatic repeat request acknowledgement (HARQ-ACK) bits transmitted in the uplink are inherently non-uniformly distributed. For such sources, significant performance gains could be obtained by employing joint source channel coding, aided by deep learning-based techniques. In this paper, we learn a transformer-based encoder using a novel "free-lunch" training algorithm and propose per-codeword power shaping to exploit the source prior at the encoder whilst being robust to small changes in the HARQ-ACK distribution. Furthermore, any HARQ-ACK decoder has to achieve a low negative acknowledgement (NACK) error rate to avoid radio link failures resulting from multiple NACK errors. We develop an extension of the Neyman-Pearson test to a coded bit system with multiple information bits to achieve Unequal Error Protection of NACK over ACK bits at the decoder. Finally, we apply the proposed encoder and decoder designs to a 5G New Radio (NR) compliant uplink setup under a fading channel, describing the optimal receiver design and a low complexity coherent approximation to it. Our results demonstrate 3-6 dB reduction in the average transmit power required to achieve the target error rates compared to the NR baseline, while also achieving a 2-3 dB reduction in the maximum transmit power, thus providing for significant coverage gains and power savings.

